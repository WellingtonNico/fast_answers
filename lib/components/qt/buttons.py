from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QTimer,pyqtSignal,pyqtSlot
from PyQt6.QtGui import *

class QDoublePushButton(QPushButton):
    doubleClicked = pyqtSignal()
    clicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        style = kwargs.pop('style',None)
        QPushButton.__init__(self, *args, **kwargs)
        if style:
            self.setStyleSheet(style)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.clicked.emit)
        super().clicked.connect(self.checkDoubleClick)

    @pyqtSlot()
    def checkDoubleClick(self):
        if self.timer.isActive():
            self.doubleClicked.emit()
            self.timer.stop()
        else:
            self.timer.start(250)