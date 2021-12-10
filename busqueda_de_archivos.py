import shelve

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from numpy import add, promote_types

#res =  False

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.res= False
        self.ask=''
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        try:
            self.path = self.cargar() 
        except:
            print('No tienes direccion de uso reciente')
        print(f'Usted recientemente busco en la direccion \n {self.path}')

        t=False
        while t == False:
            #print(type(self.ask))
            print((self.ask))
            self.ask = input('Desea buscar en la misma direccion o desea cambiar carpeta   y/n ?\n')

            if self.ask == 'y':
                self.res = True
                t = True
            else:
                t = True


        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        if  self.ask == 'n':
            addrr = self.showAddress()
            if addrr:
                self.salvar(addrr)
            #self.show()

    def busquedaArchivo(self, condicion):
        if condicion == True:
            pass

    def salvar(self, addr):
            shelfFile = shelve.open('dir')
            path = addr
            shelfFile['path'] = path
            shelfFile.close()

    def cargar(self):
        shelfFile = shelve.open('dir')
        var = str(shelfFile['path'])
        shelfFile.close()
        #print(var)
        return var

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