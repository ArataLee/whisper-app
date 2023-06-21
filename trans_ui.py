
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_main import Ui_MainWindow
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.radioGroup = QtWidgets.QButtonGroup(parent)
        self.radioGroup.addButton(self.modelButtonTiny)
        self.radioGroup.addButton(self.modelButtonSmall)
        self.radioGroup.addButton(self.modelButtonBase)
        self.radioGroup.addButton(self.modelButtonMedium)
        self.radioGroup.addButton(self.modelButtonLarge)
        self.radioGroup.addButton(self.modelButtonLargeV1)
        self.radioGroup.addButton(self.modelButtonLargeV2)
        
        self.modelButtonSmall.setChecked(True)

        self.radioGroup.buttonToggled.connect(self.radioEvent)

        self.audioSelect.clicked.connect(self.selectAudio)

        self.outputSelect.clicked.connect(self.selectOutputDir)

    def selectOutputDir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹")
        self.outputDir.setText(dir)
    
    def selectAudio(self):
        fs, type = QtWidgets.QFileDialog.getOpenFileNames(self, "选取文件", os.getcwd(), "All Files(*)")
        fileString = ""
        for v in fs:
            fileString = fileString + v + "\n"
        self.sourceAudios.setText(fileString)

    def radioEvent(self):
        self.radioGroup.checkedButton().text()

    