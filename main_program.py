from tkinter import *
from main_menu import MainMenu
from normal_mode import NormalMode
from exam_mode import ExamMode
from window_try import TryWindow
from window_win import WinWindow


def open_normal_mode(event):
    normal_mode = NormalMode(main_menu, 'backgrounds/normal_mode.png')
    normal_mode.bind('<Up>', open_exam_mode)


def open_exam_mode(event):
    global exam_mode
    exam_mode = ExamMode(main_menu, 'backgrounds/exam_mode.png')
    exam_mode.entry.bind('<Return>', open_pop_up)


def open_exam_mode_go_next():
    exam_mode.destroy()
    exam_mode_go_next = ExamMode(main_menu, 'backgrounds/exam_mode_go_next.png')
    exam_mode_go_next.bind('<Up>', exam_mode_go_next.on_close)


def open_pop_up(event):
    # здесь условие правильно или неправильно угадано
    win = True
    lose = False
    if win:
        open_exam_mode_go_next()
        WinWindow(main_menu, 'backgrounds/win.png')
    if lose:
        TryWindow(main_menu, 'backgrounds/try_again.png')


def on_close(event):
    main_menu.destroy()


main_menu = MainMenu()

# приходится запускать exam_mode вначале в основной ветке, иначе не получается сделать переход к следующему уровню
exam_mode = Toplevel()
exam_mode.destroy()


main_menu.bind('<Up>', open_normal_mode)
main_menu.bind('<Escape>', on_close)
main_menu.mainloop()
