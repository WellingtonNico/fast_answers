from datetime import datetime
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from lib.models.fast_answer import FastAnswer
from lib.screens.qt.base import BaseDialog, BaseScreen
from lib.components.qt.buttons import QDoublePushButton


class FastAnswerFormScreen(BaseDialog):
    instance:FastAnswer
    def __init__(self,instance=None) -> None:
        super().__init__()
        if instance:
            self.instance = instance
        else:
            self.instance = FastAnswer()
        self.setWindowTitle('Formulário')
        self.setFixedHeight(400)
        self.setFixedWidth(300)

        self.saveButton = QPushButton('salvar')
        self.saveButton.setStyleSheet(
            'background-color:green;color:white;font-weight:bold;border-radius:3px'
        )
        self.saveButton.clicked.connect(self.save)
        self.deleteButton = QPushButton('deletar')
        self.deleteButton.setStyleSheet(
            'background-color:red;color:white;font-weight:bold;border-radius:3px'
        )
        self.saveButton.clicked.connect(self.delete)
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(QLabel('Título:'))
        self.titleInput = QLineEdit()
        if self.instance.title:
            self.titleInput.setText(self.instance.title)
        self.mainLayout.addWidget(self.titleInput)
        self.mainLayout.addWidget(QLabel('Prioridade (quanto menor, mais acima ficará):'))
        self.priorityInput = QSpinBox()
        if self.instance.priority_number != None:
            self.priorityInput.setValue(self.instance.priority_number)
        self.mainLayout.addWidget(self.priorityInput)

        gLayout = QGridLayout()
        gLayout.addWidget(QLabel('Cor do botão:'),0,0)
        gLayout.addWidget(QLabel('Cor do texto:'),0,1)
        self.buttonColorButton = QPushButton()
        self.textColorButton = QPushButton()
        self.buttonColorButton.setStyleSheet(self.build_color_button_style(self.instance.button_color))
        self.textColorButton.setStyleSheet(self.build_color_button_style(self.instance.text_color))
        gLayout.addWidget(self.buttonColorButton,1,0)
        gLayout.addWidget(self.textColorButton,1,1)
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
    
    def build_color_button_style(self,color):
        return f'background-color:{color if color else "#ffffff"};border-radius:7px;'
    
    def save(self):
        try:
            self.instance.title = self.titleInput.text()
            self.instance.priority_number = self.priorityInput.value()
            self.instance.text = self.textInput.toPlainText()
            self.instance.save()
        except Exception as e:
            print(f'Erro: {str(e)}')

    def delete(self):
        if self.instance.id:
            try:
                self.instance.delete()
            except Exception as e:
                print(f'Erro: {str(e)}')



