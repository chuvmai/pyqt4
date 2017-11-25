#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:22:50 2017

@author: chumai
"""

import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(200,200,2000,1000)
   b.move(500,200)
   w.setWindowTitle("PyQt")
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()