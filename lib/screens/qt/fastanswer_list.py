from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from lib.screens.qt.base import BaseScreen


class FastAnswerListScreen(BaseScreen):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Respostas Rápidas')
        self.setFixedHeight(600)
        self.setFixedWidth(250)
        self.clickedTimes = 0
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.mainLayout)
        self.addButton = QPushButton('+ adicionar')
        self.mainLayout.addWidget(self.addButton)
        # self.mainLayout.addStretch()
        self.addButton.clicked.connect(lambda:self.click_addButton('ok'))

    def click_addButton(self,arg='nop'):
        self.clickedTimes += 1
        print(f'botão clicado {self.clickedTimes} {"vezes" if self.clickedTimes > 1 else "vez"}, argumento: {arg}')


