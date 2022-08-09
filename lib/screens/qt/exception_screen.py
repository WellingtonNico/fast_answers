from lib.screens.qt.base import BaseDialog
from PyQt6.QtWidgets import QLabel,QVBoxLayout
from PyQt6.QtCore import Qt


class ExceptionScreen(BaseDialog):
    def __init__(self,errors):
        super().__init__()
        if type(errors) == str:
            self.errors = errors
        elif type(errors) == dict:
            self.errors = ''
            for error in errors.values():
                self.errors += f' * - {error}\n'
        else:
            raise Exception('formato errado dos erros')
        label = QLabel(self.errors)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        label.setStyleSheet('color:red;font-weight:bold;')
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.exec()
