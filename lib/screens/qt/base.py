from PyQt6.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt6.QtGui import QIcon
from ...constants import ASSETS_DIR, ONTOP_FLAG


class BaseScreen(QWidget):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setWindowIcon(QIcon(f'{ASSETS_DIR}/icon.ico'))

    def add_on_top_flag(self):
        self.setWindowFlags(ONTOP_FLAG)


class BaseDialog(QDialog):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setWindowIcon(QIcon(f'{ASSETS_DIR}/icon.ico'))

    def add_on_top_flag(self):
        self.setWindowFlags(ONTOP_FLAG)