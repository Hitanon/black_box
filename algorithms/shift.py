#Сдвиг на Х влево/вправо
import random
from algorithms.resources import eng_alphabet

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def factory(s):
    global power
    global side
    result = ''
    if side:
        #Сдвиг вправо
        result = s[-power:]+s[:len(s)-power]
    else:
        # Сдвиг влево
        result = s[power:]+s[:power]
    if not result:
        result = '<Пусто>'
    return result

power = random.randint(1, 3)
side = bool(random.getrandbits(1))
