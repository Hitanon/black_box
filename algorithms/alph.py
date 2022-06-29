# Возвращает порядковые номера каждой буквы

import random
from algorithms.resources import eng_alphabet

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def factory(s):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newS = ''
    for i in range(len(s)):
        for j in range(33):
            if s[i] == alph[j]:
                newS += str(j+1)
                break
    if not newS:
        newS = '<Пусто>'
    return newS


