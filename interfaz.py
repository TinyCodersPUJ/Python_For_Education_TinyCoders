from gettext import install
from python_for_education.Hardware_Educacion import *
from python_for_education.install import * 
import python_for_education.s3a as s3a

import subprocess
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.iniciar)
        self.pushButton_2.clicked.connect(self.instalar)
    def instalar(self):
        if sys.platform.startswith('win32'):
            return subprocess.Popen(['python','./python_for_education/install.py'],
                                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                                                  |
                                                  subprocess.CREATE_NEW_CONSOLE)
        else:
            return subprocess.Popen(['python','./python_for_education/install.py'],
                                    stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE)
    def iniciar(self):
        ##s3a.s3ax()
        if sys.platform.startswith('win32'):
            return subprocess.Popen(['python','./python_for_education/s3a.py'],
                                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                                                  |
                                                  subprocess.CREATE_NEW_CONSOLE)
        else:
            return subprocess.Popen(['python','./python_for_education/s3a.py'],
                                    stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE)
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()