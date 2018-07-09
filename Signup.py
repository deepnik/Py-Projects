#    Signup

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
       def chkPassword(self):
        txt=self.lineEdit_2.text()
        if txt=='nikhil':
            print ('Valid password')
        elif txt=='kaur':
            print ('Valid password')
        else:
            print ('Invalid password')
            
       def chkEmail(self):
        txt=self.lineEdit.text()
        if txt=='nikhild673@gmail.com':
            print ('Valid email')
        elif txt=='kaurpoonam2326@gmail.com':
            print ('Valid email')
        else:
            print ('Invalid email')
            
     
              
              
       def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 171, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 10, 101, 21))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(60, 200, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 200, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 260, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(60, 160, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 160, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        self.pushButton_4.clicked.connect(self.lineEdit.clear)
        self.pushButton_4.clicked.connect(self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_3.clicked.connect(self.chkEmail)
        self.pushButton_3.clicked.connect(self.chkPassword)
        
       def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Email"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:1000;\">  Signup</span></p></body></html>"))
        self.checkBox.setText(_translate("Form", "Single"))
        self.checkBox_2.setText(_translate("Form", "Married"))
        self.pushButton_3.setText(_translate("Form", "Ok"))
        self.pushButton_4.setText(_translate("Form", "Reset"))
        self.radioButton.setText(_translate("Form", "Male"))
        self.radioButton_2.setText(_translate("Form", "Female"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

