# Удаляет каждый второй элемент в строке

import random
from algorithms.resources import eng_alphabet

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def  factory(s):
    newnum = ''
    for i in range(len(s)):
        if i % 2 == 0:
            newnum += s[i]
    print(newnum)
    return newnum

