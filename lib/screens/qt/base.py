from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
from ...constants import ASSETS_DIR


class BaseScreen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowIcon(QIcon(f'{ASSETS_DIR}/icon.ico'))
