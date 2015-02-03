from PyQt5 import QtCore, QtGui, QtWidgets
from core import BaiduTranslator, DailySentence


class Translator(QtWidgets.QWidget):
    def __init__(self):
        super(Translator, self).__init__()
        self.setWindowTitle("Translator")
        self.resize(240, 320)
        self.setFixedSize(self.width(), self.height())
        font = QtGui.QFont()
        font.setFamily('Microsoft YaHei UI')
        font.setPixelSize(12)
        self.setFont(font)

        self.text_in = QtWidgets.QLineEdit(self)
        self.text_in.setGeometry(QtCore.QRect(20, 10, 200, 20))

        self.text_out = QtWidgets.QTextBrowser(self)
        self.text_out.setGeometry(QtCore.QRect(20, 50, 200, 250))

        self.text_in.returnPressed.connect(self.key_event)

    def key_event(self):
        input_str = self.text_in.text()
        self.text_out.setText(BaiduTranslator.translate(input_str))

    def config_show_event(self):
        self.text_out.setText(DailySentence.get_sentence())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windows = Translator()
    windows.show()
    sys.exit(app.exec_())