from tkinter import *
from main_menu import MainMenu
from normal_mode import NormalMode
from exam_mode import ExamMode
from pop_up_window import PopUP
from window import Window

from algorithms import a_to_B
from algorithms import Caesar
from algorithms import consonant
from algorithms import dots
from algorithms import FML
from algorithms import joint
from algorithms import nine_minus_old
from algorithms import polindrome_without
from algorithms import shift
from algorithms import vowel

from algorithms import summ
from algorithms import square
from algorithms import odd_number
from algorithms import mult_number
from algorithms import length
from algorithms import every_second_del
from algorithms import even_number
from algorithms import even_odd
from algorithms import mult_two_summ_one
from algorithms import alph

import random

#Функция обработки результатов в обычном режиме
def processing(event):
    global normal_mode
    global exam_mode
    input_data = normal_mode.entry.get()
    output_data = current_level.factory(input_data)

    normal_mode.history_input['state'] = NORMAL
    normal_mode.history_output['state'] = NORMAL
    exam_mode.history_input['state'] = NORMAL
    exam_mode.history_output['state'] = NORMAL

    normal_mode.history_input.insert(0, input_data)
    normal_mode.history_output.insert(0, output_data)
    exam_mode.history_input.insert(0, input_data)
    exam_mode.history_output.insert(0, output_data)

    normal_mode.history_input['state'] = DISABLED
    normal_mode.history_output['state'] = DISABLED
    exam_mode.history_input['state'] = DISABLED
    exam_mode.history_output['state'] = DISABLED

    normal_mode.label['text'] = output_data
    normal_mode.entry.delete(0, END)


def open_normal_mode(event):
    global main_menu
    global normal_mode
    global exam_mode_go_next
    global levels
    global current_level
    # Если закончились уровни, вызывается экран о конце игры
    if len(levels):
        current_level = random.choice(levels)

        exam_mode.history_input['state'] = NORMAL
        exam_mode.history_input.delete(0, END)
        exam_mode.history_input['state'] = DISABLED
        exam_mode.history_output['state'] = NORMAL
        exam_mode.history_output.delete(0, END)
        exam_mode.history_output['state'] = DISABLED

        normal_mode = NormalMode(main_menu)
        normal_mode.bind('<Return>', processing)
        normal_mode.bind('<Up>', open_exam_mode)
        normal_mode.bind('<Escape>', on_close_normal_mode)
        main_menu.withdraw()
    else:
        end_game.deiconify()
        end_game.grab_set()



def on_close_normal_mode(event):
    global main_menu
    global normal_mode
    main_menu.deiconify()
    main_menu.grab_set()
    normal_mode.withdraw()


def open_exam_mode(event):
    global exam_mode
    global current_level
    global exam_mode
    #Генерация случайной строки текущего уровня
    input_data = current_level.get_random_string()
    normal_mode.withdraw()
    exam_mode.deiconify()
    exam_mode.grab_set()
    exam_mode.label['text'] = input_data
    exam_mode.entry.delete(0, END)
    exam_mode.entry.bind('<Return>', lambda e, data=input_data: open_pop_up(e, data))


def on_close_exam_mode(event):
    global normal_mode
    global exam_mode
    normal_mode.deiconify()
    normal_mode.grab_set()
    exam_mode.withdraw()


def open_exam_mode_go_next():
    global exam_mode_go_next
    global exam_mode
    exam_mode_go_next.deiconify()
    exam_mode_go_next.grab_set()
    exam_mode.withdraw()


def open_pop_up(event, input_data):
    global exam_mode
    global exam_mode_go_next
    global current_level
    #Проверка правильности ввода ответа на экзамене
    if exam_mode.entry.get() == current_level.factory(input_data):
        #Чтобы уровни не повторялись, текущий уровень убирается из списка
        levels.pop(levels.index(current_level))
        exam_mode_go_next.deiconify()
        exam_mode_go_next.grab_set()
        exam_mode.withdraw()
        win.deiconify()
        win.grab_set()
    else:
        lose.deiconify()
        lose.grab_set()


def on_close_win(event):
    global win
    global exam_mode_go_next
    win.withdraw()
    exam_mode_go_next.grab_set()


def on_close_lose(event):
    global lose
    global exam_mode
    lose.withdraw()
    exam_mode.entry.delete(0, END)
    exam_mode.grab_set()


def go_next_level(event):
    exam_mode_go_next.withdraw()
    open_normal_mode(event)


def on_close_end_game(event):
    global main_menu
    global end_game
    global levels
    levels = [a_to_B, nine_minus_old, Caesar, consonant, dots, FML, joint, polindrome_without, shift, vowel,
              summ, square, odd_number, mult_number, mult_two_summ_one, length, even_odd, even_number,
              every_second_del, alph]

    main_menu.deiconify()
    main_menu.grab_set()
    main_menu.bind('<Up>', open_normal_mode)
    main_menu.bind('<Escape>', on_close)

    end_game.withdraw()


def on_close(event):
    main_menu.destroy()



levels = [a_to_B, nine_minus_old, Caesar, consonant, dots, FML, joint, polindrome_without, shift, vowel,
          summ, square, odd_number, mult_number, mult_two_summ_one, length, even_odd, even_number,
          every_second_del, alph]
current_level = 0


main_menu = MainMenu()


# Инициализация всех окон и биндов
normal_mode = 0

exam_mode = ExamMode(main_menu)
exam_mode.withdraw()
exam_mode.bind('<Escape>', on_close_exam_mode)

exam_mode_go_next = Window(main_menu, 'backgrounds/exam_mode_go_next.png')
exam_mode_go_next.withdraw()
exam_mode_go_next.bind('<Up>', go_next_level)

win = PopUP(main_menu, 'backgrounds/win.png')
win.withdraw()
win.bind('<Down>', on_close_win)

lose = PopUP(main_menu, 'backgrounds/try_again.png')
lose.withdraw()
lose.bind('<Down>', on_close_lose)

end_game = Window(main_menu, 'backgrounds/end_game.png')
end_game.withdraw()
end_game.bind('<Up>', on_close_end_game)

main_menu.grab_set()
main_menu.bind('<Up>', open_normal_mode)
main_menu.bind('<Escape>', on_close)


main_menu.mainloop()
