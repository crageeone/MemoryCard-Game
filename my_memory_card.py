#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from random import shuffle, randint
#создание приложения и главного окна
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.move(370, 100)
main_win.resize(500, 350)


pal = main_win.palette()
pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#98FB98"))
pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.WindowText, QtGui.QColor("#000000"))
main_win.setPalette(pal)

#создание виджетов главного окна
LBquestion = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox("Варианты ответов")
btn_answer1 = QRadioButton("Энцы")
btn_answer2 = QRadioButton("Смурфы")
btn_answer3 = QRadioButton("Чулымцы")
btn_answer4 = QRadioButton("Алеуты")
btn_ans = QPushButton("Ответить")


RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


#расположение вариантов по лэйаутам
q_line1 = QVBoxLayout()
q_line2 = QVBoxLayout()
q_line = QHBoxLayout()

q_line1.addWidget(btn_answer1)
q_line1.addWidget(btn_answer3)
q_line2.addWidget(btn_answer2)
q_line2.addWidget(btn_answer4)


q_line.addLayout(q_line1)
q_line.addLayout(q_line2)
RadioGroupBox.setLayout(q_line)
q_line.setSpacing(5)


lay_line1 = QHBoxLayout()
lay_line2 = QHBoxLayout()
lay_line3 = QHBoxLayout()

main_line = QVBoxLayout()

lay_line1.addWidget(LBquestion, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
lay_line2.addWidget(RadioGroupBox, alignment=Qt.AlignHCenter)
lay_line3.addStretch(1)
lay_line3.addWidget(btn_ans, stretch = 2)
lay_line3.addStretch(1)
main_line.addLayout(lay_line1)
main_line.addLayout(lay_line2)
main_line.addLayout(lay_line3)


main_win.setLayout(main_line)

#вторая форма
ResultGroupBox = QGroupBox("Результат теста")
result_wr = QLabel('Ответ будет тут.')
result = QLabel('Прав ты или нет?')
res_line = QHBoxLayout()
res_line1 = QVBoxLayout()

res_line1.addWidget(result)
res_line1.addWidget(result_wr)

res_line.addLayout(res_line1)

ResultGroupBox.setLayout(res_line)
lay_line2.addWidget(ResultGroupBox, alignment=Qt.AlignHCenter)
ResultGroupBox.hide()



#обработка нажатий на переключатели
def show_question():
    ResultGroupBox.hide()
    RadioGroupBox.show()
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
    btn_ans.setText("Ответить")
def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    btn_ans.setText("Следующий вопрос")
def start_test():
    if btn_ans.text() == "Ответить":
        show_result()
    else:
        show_question()

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    LBquestion.setText(q.question)
    result_wr.setText(q.right_answer)
    show_question()
    

def show_correct(res):
    result.setText(res)
    show_result()

main_win.total = 0
main_win.score = 0

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        main_win.score+=1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Неправильно!")
questions = list()  
que1 = Question("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", "Итальянский")
que2 = Question("Какого цвета нет на флаге Италии?", "Жёлтого", "Белого","Красного","Зелёного")
que3 = Question("Что изображено на флаге Канады?", "Кленовый лист", "Дуб","Орёл","Енот")
que4 = Question("Что изображено на гербе России?","Двухглавый орёл","Два орла","Орёл","Орёл с короной")
que5 = Question("Государственный язык США","Английский","Мексиканский","Американский","Бразильский")
que6 = Question("Кто открыл Америку?","Колумб","Магелан","Пётр Первый","Робинзон Крузо")
que7 = Question("Самый популярный язык в мире","Китайский","Английский","Японский","Русский")
que8 = Question("Какого цвета нет на флаге России?","Зелёного","Белого","Синего","Красного")
que9 = Question("Сколько цветов на флаге Великобритании?","3","2","4","5")
que10 = Question("Из какого языка пришло слово Жалюзи?","Французский","Английский","Немецкий","Польский")
questions.append(que1)
questions.append(que2)
questions.append(que3)
questions.append(que4)
questions.append(que5)
questions.append(que6)
questions.append(que7)
questions.append(que8)
questions.append(que9)
questions.append(que10)


def next_question():
    cur_question = randint(0, len(questions)-1)
    q = questions[cur_question]
    ask(q)
    print("Статистика")
    print("-Всего вопросов:", main_win.total)
    print("-Правильных ответов:", main_win.score)
    if main_win.total == 0:
        main_win.total +=1
        print("Рейтинг:", str(main_win.score/main_win.total*100)+"%")
        main_win.total-=1
    else:
        print("Рейтинг:", str(main_win.score/main_win.total*100)+"%")
    main_win.total +=1

def click_OK():
    if btn_ans.text() == "Ответить":
        check_answer()
    else:
        next_question()
next_question()    
btn_ans.clicked.connect(click_OK)
#отображение окна приложения 
main_win.show()
app.exec_()