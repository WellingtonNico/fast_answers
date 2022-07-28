from screens.fast_answers_list import screen as listScreen
from lib.db.db import create_database
from lib.models.fast_answer import FastAnswer
if __name__ == '__main__':
    create_database()
    # a:FastAnswer = FastAnswer().query.first()
    # a.text = 'testando alteração'
    # a.save()
    # print(len(FastAnswer().query.all()))
    # FastAnswer().create(
    #     title='teste ok 2',text='text [saudacao] 2',text_color='#ffffff',button_color='#ffffff',priority_number=3
    # )text boa noite 2 text boa noite 2text boa noite 2
    
    # FastAnswer().create(
    #     title='teste',text='text',text_color='#ffffff',button_color='#ffffff',priority_number=3
    # )
    
    # FastAnswer().create(
    #     title='teste',text='text',text_color='#ffffff',button_color='#ffffff',priority_number=3
    # )
    

    # a.delete()
    # print(len(FastAnswer().query.all()))
    listScreen.mainloop()