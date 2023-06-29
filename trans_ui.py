
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from Ui_main import Ui_MainWindow
import os
import whisper
from whisper import utils
import threading
import torch
import logging

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
        self.transStatus = 0
        self.lock = threading.Lock()
        logging.basicConfig(filename="log.log", level=logging.DEBUG, filemode='a',format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.lock.acquire()
        transStatus = self.transStatus
        self.lock.release()
        if transStatus == 1:
            reply = QtWidgets.QMessageBox.question(self, "是否退出", "有任务进行中，是否确定退出？", QtWidgets.QMessageBox.StandardButton.Yes|QtWidgets.QMessageBox.StandardButton.No, QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                event.accept()
                os._exit(0)
            else:
                event.ignore()
                return

        event.accept()
        os._exit(0)

    def transAudios(self):
        
        output = self.output
        device = "cuda" if torch.cuda.is_available() else  "cpu"
        if device == "cpu" and torch.backends.mps.is_built():
            device = "mps"
        
        self.lock.acquire()
        self.transStatus = 1
        self.lock.release()

                
        logging.debug("started.....")
        model = whisper.load_model(self.radioGroup.checkedButton().text(), device=device)
        
        logging.debug("load model finished.....")
        logging.debug("audios:", self.audios)
        #utils.ResultWriter
        for v in self.audios:
            logging.debug("start model transcribe.....")
            result = model.transcribe(v)
            logging.debug(", ".join([i["text"] for i in result["segments"] if i is not None]))
            writer = utils.get_writer("txt", output)
            writer(result, v, {"max_line_width":"", "highlight_words":"", "max_line_count":""})
        
        logging.debug("finished.....")
        self.lock.acquire()
        self.transStatus = 0
        self.lock.release()


        #self.box.close()
        #self.box.destroy()
        #box = QtWidgets.QMessageBox()
        #box.warning(box, "转换完成", "音频转换完成, 输出位置:" + output, QtWidgets.QMessageBox.StandardButton.Close, QtWidgets.QMessageBox.StandardButton.Close)
        # finished, enable start button
        self.start.setEnabled(True)
        
    def startTrans(self):
        # check param


        t = threading.Thread(target=self.transAudios)
        t.start()

        
        #print(t.isDaemon())
        # disable start button
        self.start.setDisabled(True)

        #self.box = QtWidgets.QMessageBox()
        #self.box.warning(self, "转换中", "音频转换中, 请耐心等待...")

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

    