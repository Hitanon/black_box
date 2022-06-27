#Либо первый символ, либо средний/два средних(если длина четная), либо последний
import random
from algorithms.resources import eng_alphabet

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def factory(s):
    global side
    result = ''
    if s:
        length = len(s)
        if side == 0:
            result = s[0]
        elif side == 2:
            result = s[-1]
        elif length%2 == 1:
            result = s[length // 2]
        else:
            result = s[length//2-1:length//2+1]
    else:
        result = '<Пусто>'
    return result

side = random.randint(0, 2)
