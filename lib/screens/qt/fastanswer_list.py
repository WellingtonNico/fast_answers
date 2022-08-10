from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from lib.constants import ONTOP_FLAG,ONBOTTOM_FLAG
from lib.models.fast_answer import FastAnswer
from lib.screens.qt.base import BaseScreen
from lib.components.qt.buttons import QDoublePushButton
from lib.screens.qt.fastanswer_form import FastAnswerFormScreen
import platform
import os
if os.name != 'posix':
    try:
        import keyboard
    except:
        pass
from PyQt6.QtCore import *


class KeyBoardManager(QObject):
    signal = pyqtSignal()

    def start(self):
        keyboard.add_hotkey("ctrl+F12", self.signal.emit, suppress=True)

class FastAnswerListScreen(BaseScreen):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        if os.name != 'posix':
            manager = KeyBoardManager(self)
            manager.signal.connect(self.show_again)
            manager.start()
        self.add_on_top_flag()
        self.FastAnswerModel = FastAnswer()
        self.setWindowTitle('RA')
        self.setFixedHeight(500)
        self.setFixedWidth(190)

        self.addButton = QPushButton('+ adicionar')
        self.addButton.setStyleSheet(
            '''
            background-color:blue;
            color:white;
            font-weight:bold;
            border-radius:5px;
            padding-top:3px;
            padding-bottom-7px;
            '''
        )

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.addButton)
        # topLayout.addWidget(self.editinTriggerButton)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainLayout.addLayout(topLayout)
        self.setLayout(self.mainLayout)

        self.mainListWidget = QListWidget()
        scroll_bar = QScrollBar()
        scroll_bar.setStyleSheet(
            'width:1px'
        )
        self.mainListWidget.setVerticalScrollBar(scroll_bar)
        self.mainListWidget.setStyleSheet(
            '''
            QListWidget::item{
                margin-top:5px;margin-bottom:5px;
            }
            '''
        )
        self.mainLayout.addWidget(self.mainListWidget)
        # self.mainLayout.addStretch()
        self.addButton.clicked.connect(self.click_addButton)
        self.update_list()

    def show_again(self):
        self.showNormal()
        self.show()

    def click_addButton(self):
        form = FastAnswerFormScreen()
        form.exec()
        self.update_list()

    def open_form_screen(self):
        form = FastAnswerFormScreen(instance=self.sender().fastAnswer)
        form.exec()
        self.update_list()

    def copy_text(self):
        self.sender().fastAnswer.copy_text()
        self.showMinimized()
        self.hide()

    def update_list(self):
        self.mainListWidget.clear()
        fastAnswer:FastAnswer
        for fastAnswer in self.FastAnswerModel.get_all():
            button = QDoublePushButton(
                fastAnswer.title,
                style=f'''
                    background-color:{fastAnswer.button_color};
                    color:{fastAnswer.text_color};
                    border-radius:4px;
                '''        
            )
            button.clicked.connect(self.copy_text)
            button.rightClicked.connect(self.open_form_screen)
            button.fastAnswer = fastAnswer
            item = QListWidgetItem()
            self.mainListWidget.addItem(item)
            self.mainListWidget.setItemWidget(item,button)





