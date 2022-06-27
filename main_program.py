from tkinter import *
from main_menu import MainMenu
from normal_mode import NormalMode
from exam_mode import ExamMode
from window_try import TryWindow
from window_win import WinWindow

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


import random

def processing(event):
    global normal_mode
    input_data = normal_mode.entry.get()
    output_data = current_level.factory(input_data)
    normal_mode.history_input.insert(0, input_data)
    normal_mode.history_output.insert(0, output_data)
    normal_mode.label['text'] = output_data
    normal_mode.entry.delete(0, END)


def open_normal_mode(event):
    global normal_mode
    global levels
    global current_level
    # try:
    #     current_level = random.choice(levels)
    # except IndexError:
    #     #Закончились уровни
    #     print()
    if normal_mode:
        normal_mode.destroy()
    normal_mode = NormalMode(main_menu, 'backgrounds/normal_mode.png')
    normal_mode.bind('<Return>', processing)
    normal_mode.bind('<Up>', open_exam_mode)


def open_exam_mode(event):
    global exam_mode
    global current_level
    input_data = current_level.get_random_string()
    exam_mode = ExamMode(main_menu, 'backgrounds/exam_mode.png')
    exam_mode.label['text'] = input_data
    #По какой-то причине не получается изъять содержимое exam_mode до вызова функции
    exam_mode.entry.bind('<Return>', lambda e, input_data=input_data: open_pop_up(e, input_data))


def open_exam_mode_go_next():
    global normal_mode
    exam_mode.destroy()
    exam_mode_go_next = ExamMode(main_menu, 'backgrounds/exam_mode_go_next.png')
    exam_mode_go_next.bind('<Up>', exam_mode_go_next.on_close)
    exam_mode_go_next.bind('<Up>', open_normal_mode)


def open_pop_up(event, input_data):
    # здесь условие правильно или неправильно угадано
    global exam_mode
    global current_level
    if exam_mode.entry.get() == current_level.factory(input_data):
        levels.pop(levels.index(current_level))
        open_exam_mode_go_next()
        WinWindow(main_menu, 'backgrounds/win.png')
    else:
        TryWindow(main_menu, 'backgrounds/try_again.png')


def on_close(event):
    main_menu.destroy()


levels = [a_to_B, nine_minus_old, Caesar, consonant, dots, FML, joint, polindrome_without, shift, vowel]
current_level = levels[6]
normal_mode = 0

main_menu = MainMenu()

# # приходится запускать exam_mode вначале в основной ветке, иначе не получается сделать переход к следующему уровню
exam_mode = Toplevel()
exam_mode.destroy()

main_menu.bind('<Up>', open_normal_mode)
main_menu.bind('<Escape>', on_close)
main_menu.mainloop()
