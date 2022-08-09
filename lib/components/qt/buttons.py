from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class QDoublePushButton(QPushButton):
    doubleClicked = pyqtSignal()
    rightClicked = pyqtSignal()
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

    @pyqtSlot()
    def checkRightClick(self):
        if self.timer.isActive():
            self.rightClicked.emit()
            self.timer.stop()
        else:
            self.timer.start(250)

    def mousePressEvent(self, e) -> None:
        if e.button().name == 'RightButton':
            return self.rightClicked.emit()
        return super().mousePressEvent(e)

    