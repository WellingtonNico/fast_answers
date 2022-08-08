from PyQt6.QtWidgets import QMainWindow,QWidget,QDialog
from PyQt6.QtGui import QIcon
from ...constants import ASSETS_DIR


class BaseScreen(QWidget):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setWindowIcon(QIcon(f'{ASSETS_DIR}/icon.ico'))


class BaseDialog(QDialog):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setWindowIcon(QIcon(f'{ASSETS_DIR}/icon.ico'))
