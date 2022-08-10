from locale import windows_locale
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from lib.constants import ASSETS_DIR, ONTOP_FLAG
from lib.models.fast_answer import FastAnswer
from lib.screens.qt.base import BaseDialog
from lib.screens.qt.exception_screen import ExceptionScreen


class FastAnswerFormScreen(BaseDialog):
    instance:FastAnswer
    def __init__(self,instance=None) -> None:
        super().__init__()
        if instance:
            self.instance = instance
            self.instanceId = instance.id
        else:
            self.instance = FastAnswer()
        self.add_on_top_flag()
        self.setWindowTitle('Formulário')
        self.setFixedHeight(400)
        self.setFixedWidth(450)

        self.saveButton = QPushButton('salvar')
        self.saveButton.setStyleSheet(
            'background-color:green;color:white;font-weight:bold;border-radius:3px'
        )
        self.saveButton.clicked.connect(self.save)
        self.deleteButton = QPushButton('deletar')
        self.deleteButton.setStyleSheet(
            'background-color:red;color:white;font-weight:bold;border-radius:3px'
        )
        self.deleteButton.clicked.connect(self.delete)
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(QLabel('Título:'))
        self.titleInput = QLineEdit()
        if self.instance.title:
            self.titleInput.setText(self.instance.title)
        self.mainLayout.addWidget(self.titleInput)

        gLayout = QGridLayout()
        gLayout.addWidget(QLabel('Cor do botão:'),0,0)
        gLayout.addWidget(QLabel('Cor do texto:'),0,1)
        gLayout.addWidget(QLabel('Prioridade'),0,2)
        self.buttonColorButton = QPushButton()
        self.buttonColorButton.setStyleSheet(self.build_color_button_style(self.instance.button_color))
        self.buttonColorButton.clicked.connect(self.select_color)
        self.textColorButton = QPushButton()
        self.textColorButton.setStyleSheet(self.build_color_button_style(self.instance.text_color))
        self.textColorButton.clicked.connect(self.select_color)
        self.priorityInput = QSpinBox()
        if self.instance.priority_number != None:
            self.priorityInput.setValue(self.instance.priority_number)
        gLayout.addWidget(self.buttonColorButton,1,0)
        gLayout.addWidget(self.textColorButton,1,1)
        gLayout.addWidget(self.priorityInput)
        self.mainLayout.addLayout(gLayout)

        self.mainLayout.addWidget(QLabel('Texto da resposta rápida:'))
        self.textInput = QTextEdit()
        if self.instance.text:
            self.textInput.setText(self.instance.text)
        self.textInput.setMinimumHeight(100)
        self.mainLayout.addWidget(self.textInput)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.saveButton)
        hLayout.addWidget(self.deleteButton)
        self.mainLayout.addLayout(hLayout)

    def select_color(self):
        window = QColorDialog()
        window.setWindowFlags(ONTOP_FLAG)
        window.setWindowIcon(QIcon(f'{ASSETS_DIR}/icon.ico'))
        window.setWindowTitle('Selecione uma cor')
        if self.sender() == self.textColorButton and self.instance.text_color:
            color = QColor()
            color.setNamedColor(self.instance.text_color)
            window.setCurrentColor(color)
        elif self.sender() == self.buttonColorButton and self.instance.button_color:
            color = QColor()
            color.setNamedColor(self.instance.button_color)
            window.setCurrentColor(color)
        window.exec()
        color = window.currentColor().name()
        window.close()
        self.sender().setStyleSheet(self.build_color_button_style(color))
        if self.sender() == self.textColorButton:
            self.instance.text_color = color
        else:
            self.instance.button_color = color
    
    def build_color_button_style(self,color):
        return f'background-color:{color if color else "#ffffff"};border-radius:7px;'
    
    def save(self):
        try:
            self.instance.title = self.titleInput.text()
            self.instance.priority_number = self.priorityInput.value()
            self.instance.text = self.textInput.toPlainText()
            self.instance.button_color
            self.instance.save(**{
                'title':self.instance.title,
                'priority_number':self.instance.priority_number,
                'text':self.instance.text,
                'button_color':self.instance.button_color,
                'text_color':self.instance.text_color
            })
            self.close()
        except Exception as e:
            ExceptionScreen(str(e))

    def delete(self):
        try:
            if self.instance.id:
                try:
                    self.instance.delete()
                    self.close()
                except Exception as e:
                    print(f'Erro: {str(e)}')
        except Exception as e:
            print(e)



