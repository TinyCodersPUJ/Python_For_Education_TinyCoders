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
            # Create and show loading window immediately
            self.connection_window = ConnectionWindow()
            self.connection_window.show_loading()
            self.connection_window.show()  # Make sure the window is visible
            self.hide()  # Hide main window
            
            # Force GUI to update and show the loading window
            QtWidgets.QApplication.processEvents()
            
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
            
            # Pass the process to the connection window
            self.connection_window.set_process(self.process)
            
            # Start checking connection in background
            threading.Thread(target=self.check_connection, daemon=True).start()
            
        except Exception as e:
            if self.connection_window:
                self.connection_window.close()
            self.show()  # Show main window again
            QtWidgets.QMessageBox.critical(self, "Error", f"Error al iniciar la aplicación: {str(e)}")

    def check_connection(self):
        """Check if the connection is successful and show appropriate window"""
        time.sleep(5)  # Wait for s3a.py to initialize (increased wait time)
        
        # Check if process is still running (successful start)
        if self.process and self.process.poll() is None:
            # Process is running, show success window in main thread
            self.connection_window.success_signal.emit()
        else:
            # Process failed, show error in main thread
            self.connection_window.error_signal.emit()

    def restart_app(self):
        """Restart the application"""
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
            # Close connection window and show main window
            if self.connection_window:
                self.connection_window.close()
                self.connection_window = None
            self.process = None
            self.show()


class ConnectionWindow(QtWidgets.QDialog):
    # Define custom signals
    success_signal = QtCore.pyqtSignal()
    error_signal = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.process = None
        self.timer = None
        self.main_window = None
        
        # Connect signals to slots
        self.success_signal.connect(self.show_success)
        self.error_signal.connect(self.show_error)
        
        self.setupUi()
        
    def set_process(self, process):
        """Set the s3a.py process reference"""
        self.process = process
        
    def setupUi(self):
        self.setObjectName("ConnectionDialog")
        self.resize(400, 300)  # Increased height to accommodate all elements
        self.setWindowTitle("Hardware para Educación")
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowStaysOnTopHint)
        
        # Main layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(30, 30, 30, 30)
        
        # Status icon
        self.icon_label = QtWidgets.QLabel()
        self.icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_label.setStyleSheet("font-size: 48px;")
        self.layout.addWidget(self.icon_label)
        
        # Status message
        self.message_label = QtWidgets.QLabel()
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_label.setWordWrap(True)
        self.message_label.setStyleSheet("font: 14pt 'Satoshi'; color: rgb(51, 51, 51);")
        self.layout.addWidget(self.message_label)
        
        # Secondary message
        self.secondary_message_label = QtWidgets.QLabel()
        self.secondary_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.secondary_message_label.setWordWrap(True)
        self.secondary_message_label.setStyleSheet("font: 12pt 'Satoshi'; color: rgb(102, 102, 102);")
        self.layout.addWidget(self.secondary_message_label)
        
        # Status label
        self.status_label = QtWidgets.QLabel()
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setStyleSheet("font: 16pt 'Satoshi'; font-weight: bold;")
        self.layout.addWidget(self.status_label)
        
        # Loading progress bar (initially hidden)
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                text-align: center;
                background-color: #F5F5F5;
            }
            QProgressBar::chunk {
                background-color: #2196F3;
                border-radius: 6px;
            }
        """)
        self.layout.addWidget(self.progress_bar)
        
        # Button container
        self.button_widget = QtWidgets.QWidget()
        self.button_layout = QtWidgets.QHBoxLayout(self.button_widget)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Try again button (initially hidden)
        self.try_again_button = QtWidgets.QPushButton("Intentar de Nuevo")
        self.try_again_button.setFixedHeight(40)
        self.try_again_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(76, 175, 80);
                color: white;
                font: 12pt 'Satoshi';
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: rgb(56, 142, 60);
            }
        """)
        self.try_again_button.clicked.connect(self.try_again)
        self.try_again_button.hide()
        self.button_layout.addWidget(self.try_again_button)
        
        # Close button (initially hidden)
        self.close_button = QtWidgets.QPushButton("Cerrar Aplicación")
        self.close_button.setFixedHeight(40)
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: rgb(244, 67, 54);
                color: white;
                font: 12pt 'Satoshi';
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: rgb(211, 47, 47);
            }
        """)
        self.close_button.clicked.connect(self.close_application)
        self.close_button.hide()
        self.button_layout.addWidget(self.close_button)
        
        self.layout.addWidget(self.button_widget)

    def show_loading(self):
        """Show loading state"""
        print("DEBUG: show_loading called")  # Debug print
        
        self.icon_label.setText("⏳")
        self.icon_label.setStyleSheet("font-size: 48px; color: rgb(33, 150, 243);")
        self.message_label.setText("Conectando...")
        self.secondary_message_label.setText("Estableciendo conexión con el dispositivo")
        self.status_label.setText("Estado: Conectando")
        self.status_label.setStyleSheet("font: 16pt 'Satoshi'; font-weight: bold; color: rgb(33, 150, 243);")
        
        # Show progress bar, hide buttons
        self.progress_bar.show()
        self.try_again_button.hide()
        self.close_button.hide()
        
        # Force update
        self.update()
        self.repaint()
        
        print("DEBUG: Loading UI updated")  # Debug print

    @QtCore.pyqtSlot()
    def show_success(self):
        """Show success state"""
        print("DEBUG: show_success called")  # Debug print
        
        self.icon_label.setText("✓")
        self.icon_label.setStyleSheet("font-size: 48px; color: rgb(76, 175, 80);")
        self.message_label.setText("¡La conexión fue exitosa!")
        self.secondary_message_label.setText("No cierre esta ventana mientras use la aplicación.")
        self.status_label.setText("Estado: Conectado")
        self.status_label.setStyleSheet("font: 16pt 'Satoshi'; font-weight: bold; color: rgb(76, 175, 80);")
        
        # Hide progress bar, show only close button
        self.progress_bar.hide()
        self.try_again_button.hide()
        self.close_button.show()
        
        # Start monitoring the process
        if not self.timer:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.check_process_status)
            self.timer.start(1000)  # Check every second

    @QtCore.pyqtSlot()
    def show_error(self):
        """Show error state"""
        print("DEBUG: show_error called")  # Debug print
        
        # Show error message box first
        QtWidgets.QMessageBox.critical(self, "Error de Conexión", 
                                     "No se pudo establecer la conexión. "
                                     "Verifique que Arduino esté conectado.")
        
        # Then update the UI
        self.icon_label.setText("✗")
        self.icon_label.setStyleSheet("font-size: 48px; color: rgb(244, 67, 54);")
        self.message_label.setText("La conexión no fue exitosa.")
        self.secondary_message_label.setText("Verifique que el dispositivo esté conectado correctamente.")
        self.status_label.setText("Estado: Desconectado")
        self.status_label.setStyleSheet("font: 16pt 'Satoshi'; font-weight: bold; color: rgb(244, 67, 54);")
        
        # Hide progress bar, show both buttons
        self.progress_bar.hide()
        self.try_again_button.show()
        self.close_button.show()

    def try_again(self):
        """Try to reconnect"""
        # Get reference to main window and restart
        for widget in QtWidgets.QApplication.topLevelWidgets():
            if isinstance(widget, MainWindow):
                widget.restart_app()
                break

    def check_process_status(self):
        """Monitor the s3a.py process status"""
        if self.process and self.process.poll() is not None:
            # Process has terminated
            self.error_signal.emit()
            
            if self.timer:
                self.timer.stop()
                self.timer = None

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