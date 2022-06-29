# произведение чисел

import random

def get_random_string():
    return str(random.randint(100, 999))

def factory(s):
    mul = 1
    flag = True
    for i in s:
        if not (i.isdigit() or i == '-'):
            flag = False
    if flag:
        s = abs(int(s))
        while s != 0:
            mul *= s % 10
            s = s // 10
    else:
        mul = '<Пусто>'
    return str(mul)

