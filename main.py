import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_conversor(object):
    def setupUi(self, conversor):
        conversor.setObjectName("conversor")
        conversor.resize(470, 428)
        conversor.setStyleSheet("")
        self.botao_converter = QtWidgets.QPushButton(conversor)
        self.botao_converter.setGeometry(QtCore.QRect(80, 360, 75, 23))
        self.botao_converter.setObjectName("botao_converter")
        self.botao_sair = QtWidgets.QPushButton(conversor)
        self.botao_sair.setGeometry(QtCore.QRect(320, 360, 75, 23))
        self.botao_sair.setObjectName("botao_sair")
        self.label = QtWidgets.QLabel(conversor)
        self.label.setGeometry(QtCore.QRect(130, 160, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(conversor)
        self.label_2.setGeometry(QtCore.QRect(130, 50, 221, 41))
        self.label_2.setStyleSheet("color: rgb(170, 85, 127);")
        self.label_2.setObjectName("label_2")
        self.entrada_temperatura = QtWidgets.QLineEdit(conversor)
        self.entrada_temperatura.setGeometry(QtCore.QRect(220, 160, 131, 20))
        self.entrada_temperatura.setObjectName("entrada_temperatura")

        self.retranslateUi(conversor)
        QtCore.QMetaObject.connectSlotsByName(conversor)
        self.botao_converter.clicked.connect(self.converter)

    def converter(self):
        temp = self.entrada_temperatura.text()
        temp = (temp-32) * 5/9

        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Sucesso")
        msg.setText("Resultado:"+str(temp)+"c")
        msg.exec()

    def retranslateUi(self, conversor):
        _translate = QtCore.QCoreApplication.translate
        conversor.setWindowTitle(_translate("conversor", "Form"))
        self.botao_converter.setText(_translate("conversor", "Converter"))
        self.botao_sair.setText(_translate("conversor", "Sair"))
        self.label.setText(_translate("conversor", "<html><head/><body><p><span style=\" font-weight:600;\">Temperatura:</span></p></body></html>"))
        self.label_2.setText(_translate("conversor", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Conversor de temperatura</span></p></body></html>"))

app = QtWidgets.QApplication(sys.argv)
janela = QtWidgets.QMainWindow()
objeto = Ui_conversor()
objeto.setupUi(janela)
janela.show()
app.exec_()