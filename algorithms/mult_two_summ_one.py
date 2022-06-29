# Умножить на 2 и прибаваляет 1 к числу
import random

def get_random_string():
    return str(random.randint(100, 999))

def factory(s):
    newnum = ''
    flag = True
    for i in s:
        if not (i.isdigit() or i == '-'):
            flag = False
    if flag:
        s = int(s)
        newnum = s * 2 + 1
    if not newnum:
        newnum = '<Пусто>'
    return str(newnum)
