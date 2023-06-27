
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_main import Ui_MainWindow
import os
import whisper
from whisper import utils
import threading

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
        self.start.clicked.connect(self.startTrans)

        self.audios = None
        self.output = None

    def transAudios(self):
        model = whisper.load_model(self.radioGroup.checkedButton().text())
        
        # 新启线程执行转换
        #utils.ResultWriter
        for v in self.audios:
            result = model.transcribe(v)
            print(", ".join([i["text"] for i in result["segments"] if i is not None]))
            writer = utils.get_writer("all", self.output)
            writer(result, v, {"max_line_width":"", "highlight_words":"", "max_line_count":""})
        
        # finished, enable start button
        self.start.setEnabled(True)
    
    def startTrans(self):
        t = threading.Thread(target=self.transAudios)
        t.start()
        # disable start button
        self.start.setDisabled(True)

    def selectOutputDir(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹")
        self.outputDir.setText(dir)
        self.output = dir
    
    def selectAudio(self):
        fs, type = QtWidgets.QFileDialog.getOpenFileNames(self, "选取文件", os.getcwd(), "All Files(*)")
        fileString = ""
        for v in fs:
            fileString = fileString + v + "\n"
        self.sourceAudios.setText(fileString)
        self.audios = fs

    def radioEvent(self):
        self.radioGroup.checkedButton().text()

    