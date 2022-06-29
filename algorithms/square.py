#Возводит число в квадрат

import random

def get_random_string():
    return str(random.randint(100, 999))

def factory(s):
    k = ''
    flag = True
    for i in s:
        if not (i.isdigit() or i == '-'):
            flag = False
    if flag:
        s = int(s)
        k = s * s
    else:
        k = '<Пусто>'
    return str(k)
