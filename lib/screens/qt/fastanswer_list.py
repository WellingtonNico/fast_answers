import copy
from datetime import datetime
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from lib.models.fast_answer import FastAnswer
from lib.screens.qt.base import BaseScreen
from lib.components.qt.buttons import QDoublePushButton
from lib.screens.qt.fastanswer_form import FastAnswerFormScreen


class FastAnswerListScreen(BaseScreen):
    is_on_editin_mode = False
    editinTriggerButtonText = 'E'
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.FastAnswerModel = FastAnswer()
        self.setWindowTitle('Respostas Rápidas')
        self.setFixedHeight(600)
        self.setFixedWidth(250)

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

    def click_addButton(self):
        form = FastAnswerFormScreen()
        form.exec()
        self.update_list()

    def fast_answer_clicked(self,fastAnswer:FastAnswer):
        if (datetime.now()-self.lastClick).seconds < 1:
            print('abrindo edição')
        else:
            fastAnswer.copy_text()
        self.lastClick = datetime.now()

    def open_form_screen(self):
        form = FastAnswerFormScreen(instance=self.sender().fastAnswer)
        form.exec()
        self.update_list()

    def copy_text(self):
        self.sender().fastAnswer.copy_text()

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
            button.doubleClicked.connect(self.open_form_screen)
            button.fastAnswer = fastAnswer
            item = QListWidgetItem()
            self.mainListWidget.addItem(item)
            self.mainListWidget.setItemWidget(item,button)





