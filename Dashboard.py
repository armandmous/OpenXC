# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:38:15 2019

@author: arman
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon

print('Running OpenXC Dashboard...')

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'OpenXC Dashboard'
        '''self.left = 10
        self.top = 10
        self.width = 1650
        self.height = 1500'''
        self.initUI()
        
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setWindowState(QIcon.Qt.WindowMaximized)
        self.showMaximized()
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())