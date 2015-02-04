#!/usr/env/python3
# -*-coding:utf-8-*-

"""
documentary
"""

from PyQt5 import QtWidgets, QtGui, QtCore
import sys

__author__ = 'skitta'


class Widget(QtWidgets):
    def __init__(self):
        super(Widget, self).__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.widget = QtWidgets.QWidget()

        self.widget.setWindowTitle('Translator')
        self.widget.resize(240, 320)
        self.widget.setFixedSize(self.width(), self.height())
        font = QtGui.QFont()
        font.setFamily('Microsoft YaHei UI')
        font.setPixelSize(12)
        self.widget.setFont(font)

        self.widget.text_in = QtWidgets.QLineEdit(self)
        self.widget.text_in.setGeometry(QtCore.QRect(20, 10, 200, 20))
        self.widget.text_out = QtWidgets.QTextBrowser(self)
        self.widget.text_out.setGeometry(QtCore.QRect(20, 50, 200, 250))

    def run(self):
        window = Widget()
        window.show()
        sys.exit(self.app.exec_())