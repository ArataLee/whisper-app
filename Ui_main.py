# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\workspace\code\py\voicetotext\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.outputDir = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputDir.setObjectName("outputDir")
        self.gridLayout.addWidget(self.outputDir, 5, 3, 5, 1)
        self.audioSelect = QtWidgets.QPushButton(self.centralwidget)
        self.audioSelect.setObjectName("audioSelect")
        self.gridLayout.addWidget(self.audioSelect, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.modelButtonMedium = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonMedium.setObjectName("modelButtonMedium")
        self.gridLayout.addWidget(self.modelButtonMedium, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.modelButtonBase = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonBase.setObjectName("modelButtonBase")
        self.gridLayout.addWidget(self.modelButtonBase, 6, 0, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 9, 2, 1, 1)
        self.sourceAudios = QtWidgets.QTextBrowser(self.centralwidget)
        self.sourceAudios.setObjectName("sourceAudios")
        self.gridLayout.addWidget(self.sourceAudios, 1, 0, 1, 4)
        self.modelButtonLargeV1 = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonLargeV1.setObjectName("modelButtonLargeV1")
        self.gridLayout.addWidget(self.modelButtonLargeV1, 7, 1, 1, 1)
        self.modelButtonTiny = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonTiny.setObjectName("modelButtonTiny")
        self.gridLayout.addWidget(self.modelButtonTiny, 5, 0, 1, 1)
        self.modelButtonSmall = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonSmall.setObjectName("modelButtonSmall")
        self.gridLayout.addWidget(self.modelButtonSmall, 7, 0, 1, 1)
        self.modelButtonLarge = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonLarge.setObjectName("modelButtonLarge")
        self.gridLayout.addWidget(self.modelButtonLarge, 6, 1, 1, 1)
        self.modelButtonLargeV2 = QtWidgets.QRadioButton(self.centralwidget)
        self.modelButtonLargeV2.setObjectName("modelButtonLargeV2")
        self.gridLayout.addWidget(self.modelButtonLargeV2, 8, 0, 1, 1)
        self.outputSelect = QtWidgets.QPushButton(self.centralwidget)
        self.outputSelect.setObjectName("outputSelect")
        self.gridLayout.addWidget(self.outputSelect, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.progress = QtWidgets.QTextBrowser(self.centralwidget)
        self.progress.setObjectName("progress")
        self.gridLayout.addWidget(self.progress, 3, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "语音转文字"))
        self.audioSelect.setText(_translate("MainWindow", "选择音频"))
        self.label_4.setText(_translate("MainWindow", "结果输出位置:"))
        self.modelButtonMedium.setText(_translate("MainWindow", "medium"))
        self.label_3.setText(_translate("MainWindow", "模型选择:"))
        self.modelButtonBase.setText(_translate("MainWindow", "base"))
        self.start.setText(_translate("MainWindow", "开始转换"))
        self.modelButtonLargeV1.setText(_translate("MainWindow", "lagre-v1"))
        self.modelButtonTiny.setText(_translate("MainWindow", "tiny"))
        self.modelButtonSmall.setText(_translate("MainWindow", "small"))
        self.modelButtonLarge.setText(_translate("MainWindow", "lagre"))
        self.modelButtonLargeV2.setText(_translate("MainWindow", "lagre-v2"))
        self.outputSelect.setText(_translate("MainWindow", "选择输出目录"))
        self.label.setText(_translate("MainWindow", "源文件:"))
        self.label_2.setText(_translate("MainWindow", "转换进度:"))