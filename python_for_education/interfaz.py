from Hardware_Educacion import * 

import subprocess
import sys
import time
import threading

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.iniciar)
        self.pushButton_2.hide()
        self.connection_window = None
        self.process = None

    def iniciar(self):
        try:
            # Start the s3a.py process without showing terminal
            if sys.platform.startswith('win32'):
                self.process = subprocess.Popen(['python','./s3a.py'],
                                              creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                                                            |
                                                            subprocess.CREATE_NO_WINDOW,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
            else:
                self.process = subprocess.Popen(['python','./s3a.py'],
                                              stdin=subprocess.PIPE, 
                                              stderr=subprocess.PIPE,
                                              stdout=subprocess.PIPE)
            
            # Wait a moment for the process to initialize
            threading.Thread(target=self.check_connection, daemon=True).start()
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error al iniciar la aplicación: {str(e)}")

    def check_connection(self):
        """Check if the connection is successful and show success window"""
        time.sleep(3)  # Wait for s3a.py to initialize
        
        # Check if process is still running (successful start)
        if self.process and self.process.poll() is None:
            # Process is running, show success window in main thread
            QtCore.QMetaObject.invokeMethod(self, "show_connection_success", 
                                          QtCore.Qt.QueuedConnection)
        else:
            # Process failed, show error in main thread
            QtCore.QMetaObject.invokeMethod(self, "show_connection_error", 
                                          QtCore.Qt.QueuedConnection)

    @QtCore.pyqtSlot()
    def show_connection_success(self):
        """Show the connection success window"""
        self.connection_window = ConnectionWindow(self.process)
        self.connection_window.show()
        
        # Hide the main window
        self.hide()

    @QtCore.pyqtSlot()
    def show_connection_error(self):
        """Show error message if connection failed"""
        QtWidgets.QMessageBox.critical(self, "Error de Conexión", 
                                     "No se pudo establecer la conexión. "
                                     "Verifique que Arduino esté conectado.")


class ConnectionWindow(QtWidgets.QDialog):
    def __init__(self, process):
        super().__init__()
        self.process = process
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("ConnectionDialog")
        self.resize(400, 200)
        self.setWindowTitle("Hardware para Educación - Conexión Exitosa")
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        # Main layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Success icon/image (optional)
        icon_label = QtWidgets.QLabel()
        icon_label.setAlignment(QtCore.Qt.AlignCenter)
        icon_label.setStyleSheet("font-size: 48px; color: rgb(76, 175, 80);")
        icon_label.setText("✓")
        layout.addWidget(icon_label)
        
        # Success message
        message_label = QtWidgets.QLabel()
        message_label.setAlignment(QtCore.Qt.AlignCenter)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("font: 14pt 'Satoshi'; color: rgb(51, 51, 51);")
        message_label.setText("¡La conexión fue exitosa!\n\nNo cierre esta ventana mientras use la aplicación.")
        layout.addWidget(message_label)
        
        # Status label
        self.status_label = QtWidgets.QLabel()
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setStyleSheet("font: 10pt 'Satoshi'; color: rgb(76, 175, 80);")
        self.status_label.setText("Estado: Conectado")
        layout.addWidget(self.status_label)
        
        # Close button
        self.close_button = QtWidgets.QPushButton("Cerrar Aplicación")
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(244, 67, 54);
                color: white;
                font: 12pt 'Satoshi';
                border: none;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgb(211, 47, 47);
            }
        """)
        self.close_button.clicked.connect(self.close_application)
        layout.addWidget(self.close_button)
        
        # Start monitoring the process
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_process_status)
        self.timer.start(1000)  # Check every second

    def check_process_status(self):
        """Monitor the s3a.py process status"""
        if self.process and self.process.poll() is not None:
            # Process has terminated
            self.status_label.setText("Estado: Desconectado")
            self.status_label.setStyleSheet("font: 10pt 'Satoshi'; color: rgb(244, 67, 54);")
            
            # Show error message
            QtWidgets.QMessageBox.warning(self, "Conexión Perdida", 
                                        "La conexión se ha perdido. "
                                        "Verifique que Arduino esté conectado.")
            
            self.timer.stop()

    def close_application(self):
        """Close the application and terminate the s3a.py process"""
        try:
            if self.process and self.process.poll() is None:
                # Terminate the s3a.py process
                if sys.platform.startswith('win32'):
                    subprocess.run(['taskkill', '/F', '/T', '/PID', str(self.process.pid)], 
                                 creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    self.process.terminate()
                    self.process.wait(timeout=5)
        except Exception as e:
            print(f"Error closing process: {e}")
        finally:
            QtWidgets.QApplication.quit()

    def closeEvent(self, event):
        """Handle window close event"""
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar Aplicación', 
                                             "¿Está seguro que desea cerrar la aplicación?",
                                             QtWidgets.QMessageBox.Yes | 
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
            self.close_application()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()