# from lib.screens.fastanswer_list import FastAnswerListScreen
from lib.db.db import create_database
from PyQt6.QtWidgets import QApplication
from lib.models.fast_answer import FastAnswer
from lib.screens.qt.fastanswer_list import FastAnswerListScreen
import sys


if __name__ == '__main__':
    create_database()
    # a:FastAnswer = FastAnswer().query.first()
    # a.text = 'testando alteração'
    # a.save()
    print(len(FastAnswer().query.all()))
    # FastAnswer().query.delete()
    # for priority in range(5,0,-1):
    #     FastAnswer().create(
    #         title=f'teste ok prioridade {priority}',text=f'text [saudacao] {priority}',text_color='#000303',button_color='#42f5f2',priority_number=priority,
    #     )
    
    # # FastAnswer().create(
    #     title='teste',text='text',text_color='#ffffff',button_color='#ffffff',priority_number=3
    # )
    
    # FastAnswer().create(
    #     title='teste',text='text',text_color='#ffffff',button_color='#ffffff',priority_number=3
    # )
    

    # a.delete()
    print(len(FastAnswer().query.all()))
    app = QApplication(sys.argv)
    mainScreen = FastAnswerListScreen()
    mainScreen.show()
    sys.exit(app.exec())
    # FastAnswerListScreen().mainloop()
    # mainScreen.mainloop()