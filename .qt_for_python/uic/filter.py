# Form implementation generated from reading ui file '/Users/sree/First2/CS3200/project/ui_files/filter.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fee_box = QtWidgets.QTextEdit(self.centralwidget)
        self.fee_box.setGeometry(QtCore.QRect(170, 50, 111, 31))
        self.fee_box.setObjectName("fee_box")
        self.fee_label = QtWidgets.QLabel(self.centralwidget)
        self.fee_label.setGeometry(QtCore.QRect(20, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label.setFont(font)
        self.fee_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label.setObjectName("fee_label")
        self.filter_universities_label = QtWidgets.QLabel(self.centralwidget)
        self.filter_universities_label.setGeometry(QtCore.QRect(130, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.filter_universities_label.setFont(font)
        self.filter_universities_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.filter_universities_label.setObjectName("filter_universities_label")
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(290, 50, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label.setFont(font)
        self.to_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label.setObjectName("to_label")
        self.fee_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.fee_box_2.setGeometry(QtCore.QRect(330, 50, 111, 31))
        self.fee_box_2.setObjectName("fee_box_2")
        self.tuition_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.tuition_box_2.setGeometry(QtCore.QRect(330, 100, 111, 31))
        self.tuition_box_2.setObjectName("tuition_box_2")
        self.tuition_box = QtWidgets.QTextEdit(self.centralwidget)
        self.tuition_box.setGeometry(QtCore.QRect(170, 100, 111, 31))
        self.tuition_box.setObjectName("tuition_box")
        self.fee_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_2.setGeometry(QtCore.QRect(20, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_2.setFont(font)
        self.fee_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_2.setObjectName("fee_label_2")
        self.to_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_2.setGeometry(QtCore.QRect(290, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_2.setFont(font)
        self.to_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_2.setObjectName("to_label_2")
        self.to_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_3.setGeometry(QtCore.QRect(290, 200, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_3.setFont(font)
        self.to_label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_3.setObjectName("to_label_3")
        self.aid_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.aid_box_2.setGeometry(QtCore.QRect(330, 150, 111, 31))
        self.aid_box_2.setObjectName("aid_box_2")
        self.sat_box = QtWidgets.QTextEdit(self.centralwidget)
        self.sat_box.setGeometry(QtCore.QRect(170, 200, 111, 31))
        self.sat_box.setObjectName("sat_box")
        self.fee_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_3.setGeometry(QtCore.QRect(20, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_3.setFont(font)
        self.fee_label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_3.setObjectName("fee_label_3")
        self.aid_box = QtWidgets.QTextEdit(self.centralwidget)
        self.aid_box.setGeometry(QtCore.QRect(170, 150, 111, 31))
        self.aid_box.setObjectName("aid_box")
        self.fee_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_4.setGeometry(QtCore.QRect(20, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_4.setFont(font)
        self.fee_label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_4.setObjectName("fee_label_4")
        self.to_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_4.setGeometry(QtCore.QRect(290, 150, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_4.setFont(font)
        self.to_label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_4.setObjectName("to_label_4")
        self.sat_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.sat_box_2.setGeometry(QtCore.QRect(330, 200, 111, 31))
        self.sat_box_2.setObjectName("sat_box_2")
        self.to_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_5.setGeometry(QtCore.QRect(290, 300, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_5.setFont(font)
        self.to_label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_5.setObjectName("to_label_5")
        self.campus_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.campus_box_2.setGeometry(QtCore.QRect(330, 350, 111, 31))
        self.campus_box_2.setObjectName("campus_box_2")
        self.fee_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_5.setGeometry(QtCore.QRect(20, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_5.setFont(font)
        self.fee_label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_5.setObjectName("fee_label_5")
        self.rank_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.rank_box_2.setGeometry(QtCore.QRect(330, 250, 111, 31))
        self.rank_box_2.setObjectName("rank_box_2")
        self.acceptance_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.acceptance_box_2.setGeometry(QtCore.QRect(330, 400, 111, 31))
        self.acceptance_box_2.setObjectName("acceptance_box_2")
        self.to_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_6.setGeometry(QtCore.QRect(290, 350, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_6.setFont(font)
        self.to_label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_6.setObjectName("to_label_6")
        self.body_box = QtWidgets.QTextEdit(self.centralwidget)
        self.body_box.setGeometry(QtCore.QRect(170, 300, 111, 31))
        self.body_box.setObjectName("body_box")
        self.fee_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_6.setGeometry(QtCore.QRect(20, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_6.setFont(font)
        self.fee_label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_6.setObjectName("fee_label_6")
        self.acceptance_box = QtWidgets.QTextEdit(self.centralwidget)
        self.acceptance_box.setGeometry(QtCore.QRect(170, 400, 111, 31))
        self.acceptance_box.setObjectName("acceptance_box")
        self.rank_box = QtWidgets.QTextEdit(self.centralwidget)
        self.rank_box.setGeometry(QtCore.QRect(170, 250, 111, 31))
        self.rank_box.setObjectName("rank_box")
        self.fee_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_7.setGeometry(QtCore.QRect(20, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_7.setFont(font)
        self.fee_label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_7.setObjectName("fee_label_7")
        self.fee_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.fee_label_8.setGeometry(QtCore.QRect(20, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fee_label_8.setFont(font)
        self.fee_label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fee_label_8.setObjectName("fee_label_8")
        self.to_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_7.setGeometry(QtCore.QRect(290, 250, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_7.setFont(font)
        self.to_label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_7.setObjectName("to_label_7")
        self.to_label_8 = QtWidgets.QLabel(self.centralwidget)
        self.to_label_8.setGeometry(QtCore.QRect(290, 400, 31, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.to_label_8.setFont(font)
        self.to_label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.to_label_8.setObjectName("to_label_8")
        self.body_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.body_box_2.setGeometry(QtCore.QRect(330, 300, 111, 31))
        self.body_box_2.setObjectName("body_box_2")
        self.campus_box = QtWidgets.QTextEdit(self.centralwidget)
        self.campus_box.setGeometry(QtCore.QRect(170, 350, 111, 31))
        self.campus_box.setObjectName("campus_box")
        self.shutdown_db_button = QtWidgets.QPushButton(self.centralwidget)
        self.shutdown_db_button.setGeometry(QtCore.QRect(310, 500, 151, 31))
        self.shutdown_db_button.setObjectName("shutdown_db_button")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(0, 500, 81, 31))
        self.back_button.setObjectName("back_button")
        self.filter_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_button.setGeometry(QtCore.QRect(180, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filter_button.setFont(font)
        self.filter_button.setObjectName("filter_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fee_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.fee_label.setText(_translate("MainWindow", "Application Fee:"))
        self.filter_universities_label.setText(_translate("MainWindow", "Filter Universities"))
        self.to_label.setText(_translate("MainWindow", "to"))
        self.fee_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">90</p></body></html>"))
        self.tuition_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">62000</p></body></html>"))
        self.tuition_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.fee_label_2.setText(_translate("MainWindow", "Tuition:"))
        self.to_label_2.setText(_translate("MainWindow", "to"))
        self.to_label_3.setText(_translate("MainWindow", "to"))
        self.aid_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">64000</p></body></html>"))
        self.sat_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">400</p></body></html>"))
        self.fee_label_3.setText(_translate("MainWindow", "Average SAT:"))
        self.aid_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.fee_label_4.setText(_translate("MainWindow", "Average Aid:"))
        self.to_label_4.setText(_translate("MainWindow", "to"))
        self.sat_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1600</p></body></html>"))
        self.to_label_5.setText(_translate("MainWindow", "to"))
        self.campus_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8700</p></body></html>"))
        self.fee_label_5.setText(_translate("MainWindow", "Acceptance Rate:"))
        self.rank_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20</p></body></html>"))
        self.acceptance_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20</p></body></html>"))
        self.to_label_6.setText(_translate("MainWindow", "to"))
        self.body_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.fee_label_6.setText(_translate("MainWindow", "Student Body:"))
        self.acceptance_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.rank_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.fee_label_7.setText(_translate("MainWindow", "Ranking:"))
        self.fee_label_8.setText(_translate("MainWindow", "Campus Size:"))
        self.to_label_7.setText(_translate("MainWindow", "to"))
        self.to_label_8.setText(_translate("MainWindow", "to"))
        self.body_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">32000</p></body></html>"))
        self.campus_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.shutdown_db_button.setText(_translate("MainWindow", "Shutdown Database"))
        self.back_button.setText(_translate("MainWindow", "Go Back"))
        self.filter_button.setText(_translate("MainWindow", "FILTER"))
