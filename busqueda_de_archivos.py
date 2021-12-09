import shelve
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from numpy import add, promote_types
import re
from termcolor import colored
import subprocess
#res =  False
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.path = ''
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
            self.ask = input(colored('Desea buscar en la misma direccion o desea cambiar carpeta   y/n ?\n', 'red', attrs=['reverse', 'blink']))

            if self.ask == 'y':
                self.res = True
                t = True
            else:
                t = True


        #self.openFileNameDialog()
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        self.listado = []
        if  self.ask == 'n':
            addrr = self.showAddress()
            if addrr:
                self.salvar(addrr)
        else:
            addrr= self.path
        self.listado = self.busquedaArchivo(True, addrr+'/')
        self.seleccionar_archivo(self.listado, addrr)
        #print (self.listado)
            #self.show()

    def busquedaArchivo(self, condicion, direccion):
        BUSQUEDA = ''
        pa = BUSQUEDA+'.*.pdf'
        pattern  = re.compile(pa, re.I)
        lista = []
        if condicion == True:
            for filename in os.listdir(direccion):
                res =re.match(pattern, str(filename) )
                if res:
                    #lista.append([lineas, str(cant)])
                    print(colored(filename))
                    lista.append(filename)
                    #os.system(direccion+'/'+filename)
        return lista
                    #print (filename)

    def seleccionar_archivo(self, lista, direccion):
        contador = 0
        print('Los archivosencontrados mas parecidos son los siguientes: \n')
        for name in lista:
            contador+=1
            print(str(contador)+' - ' + name)

        resp = int(input('Cual de ellos desea abrir?, indique el numero que le corresponde \n'))
        os.system('\"'+ direccion+'/'+str(lista[resp-1])+'\"')
        #os.system('\"'+direccion+'/'+'competitive programming handbook.pdf\"')
        #subprocess.call(direccion+'/'+lista[resp-1])
        #print(lista[resp-1])


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