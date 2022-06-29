# Количество точек в символах
import random
from algorithms.resources import dots

def get_random_string():
    return ''.join(random.choice(dots) for i in range(random.choice((3, 4))))


def factory(s):
    symbols = {'ё': 2, '%': 2, ':': 2, '!': 1, '№': 1, ';': 1, '?': 1, '.': 1, 'i': 1, 'j': 1}
    result = 0
    for i in s:
        if i in dots:
            result += symbols[i]
    return str(result)
