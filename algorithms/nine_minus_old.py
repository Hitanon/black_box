# Если цифра четная(не ноль), то (9-цифра), иначе цифра
import random


def get_random_string():
    return str(random.randint(100, 999))


def factory(x):
    result = ''
    flag = True
    for i in x:
        if not (i.isdigit() or i == '-'):
            flag = False
    if flag:
        if x[0] != '-':
            flag = False
        x = abs(int(x))
        while x:
            last = x % 10
            if last % 2 == 0:
                result = str(9 - last) + result
            else:
                result = str(last) + result
            x //= 10
        if flag:
            result = '-' + result
    else:
        result = '<Пусто>'
    return result