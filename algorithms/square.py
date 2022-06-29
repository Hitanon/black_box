#Возводит число в квадрат

import random

def get_random_string():
    return str(random.randint(100, 999))

def factory(s):
    k = ''
    if s.isdigit():
        s = int(s)
        k = s * s
    if not k:
        k = '<Пусто>'
    return str(k)


