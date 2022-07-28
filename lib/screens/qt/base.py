from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon

class BaseScreen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowIcon(QIcon('./../../assets/icon.ico'))
