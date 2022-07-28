from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from lib.screens.qt.base import BaseScreen


class FastAnswerListScreen(BaseScreen):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Respostas Rápidas')
        self.setFixedHeight(600)
        self.setFixedWidth(250)

