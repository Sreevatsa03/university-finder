# Form implementation generated from reading ui file '/Users/sree/First2/CS3200/project/ui_files/edit_notes.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shutdown_db_button = QtWidgets.QPushButton(self.centralwidget)
        self.shutdown_db_button.setGeometry(QtCore.QRect(330, 300, 151, 31))
        self.shutdown_db_button.setObjectName("shutdown_db_button")
        self.name_box = QtWidgets.QTextEdit(self.centralwidget)
        self.name_box.setGeometry(QtCore.QRect(90, 60, 111, 31))
        self.name_box.setObjectName("name_box")
        self.notes_box = QtWidgets.QTextEdit(self.centralwidget)
        self.notes_box.setGeometry(QtCore.QRect(90, 110, 371, 111))
        self.notes_box.setObjectName("notes_box")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(20, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.notes_label = QtWidgets.QLabel(self.centralwidget)
        self.notes_label.setGeometry(QtCore.QRect(20, 110, 61, 31))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.notes_label.setFont(font)
        self.notes_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.notes_label.setObjectName("notes_label")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(0, 300, 81, 31))
        self.back_button.setObjectName("back_button")
        self.edit_notes_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_notes_button.setGeometry(QtCore.QRect(180, 240, 111, 31))
        self.edit_notes_button.setObjectName("edit_notes_button")
        self.add_watchlist_label = QtWidgets.QLabel(self.centralwidget)
        self.add_watchlist_label.setGeometry(QtCore.QRect(140, 0, 191, 41))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_watchlist_label.setFont(font)
        self.add_watchlist_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.add_watchlist_label.setObjectName("add_watchlist_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 24))
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
        self.shutdown_db_button.setText(_translate("MainWindow", "Shutdown Database"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.notes_label.setText(_translate("MainWindow", "Notes:"))
        self.back_button.setText(_translate("MainWindow", "Go Back"))
        self.edit_notes_button.setText(_translate("MainWindow", "Edit"))
        self.add_watchlist_label.setText(_translate("MainWindow", "Edit Notes:"))
