#Делаем реверс числа, если цифра четная  увеличиваем,нечетное ументьшаем

import random

def get_random_string():
    return str(random.randint(100, 999))

def  factory(s):
    newnum = ''
    if s.isdigit():
        s = int(s)
        while s != 0:
            digit = s % 10
            if digit % 2 == 0:
                newnum += str(digit + 1)
            else:
                newnum += str(digit - 1)
            s = s // 10
    if not newnum:
        newnum = '<Пусто>'
    return str(newnum)
