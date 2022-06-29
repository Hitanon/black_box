# Работает с латинским алфавитом
# Возвращает порядковые номера каждой буквы

import random
from algorithms.resources import eng_alphabet

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def factory(s):
    newS = ''
    s = s.lower()
    for i in s:
        if i in eng_alphabet:
            newS += str(eng_alphabet.index(i)+1)
    if not newS:
        newS = '<Пусто>'
    return newS


