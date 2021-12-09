import shelve

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from numpy import add

ask =  False

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.cargar() 

        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        addrr = self.showAddress()

        self.salvar(addrr)
        #self.show()

    def salvar(self, addr):
            shelfFile = shelve.open('dir')
            path = addr
            shelfFile['path'] = path
            shelfFile.close()

    def cargar(self):
        shelfFile = shelve.open('dir')
        print(shelfFile['path'])
        shelfFile.close()

    def showAddress(self, directory=''): # C:/
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        #options |= QFileDialog.DontUseCustomDirectoryIcons
        #dialog = QFileDialog()
        #dialog.setOptions(options)

        #dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)   
        dialog = QFileDialog()
        foo_dir = dialog.getExistingDirectory(self, '')

        if directory != '':
            dialog.setDirectory(str(directory))
        else:
            pass

        print(foo_dir) 
        self.close()
        return foo_dir


path = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    #sys.exit(app.exec_())
    #sys.exit(ex.exec_())