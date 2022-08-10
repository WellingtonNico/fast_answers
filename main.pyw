from lib.db.db import create_database
from PyQt6.QtWidgets import QApplication
from lib.models.fast_answer import FastAnswer
from lib.screens.qt.fastanswer_list import FastAnswerListScreen
import sys


if __name__ == '__main__':
    mainScreen:FastAnswerListScreen

    create_database()

    print(len(FastAnswer().query.all()))

    print(len(FastAnswer().query.all()))
    app = QApplication(sys.argv)
    mainScreen = FastAnswerListScreen()
    # mainScreen.show()
    sys.exit(app.exec())
