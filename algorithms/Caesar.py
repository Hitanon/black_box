# Шифр Цезаря. Загадывается число(power) и сторона(side)
# Каждая буква сдвигается в алфавите на x позиций в сторону
import random
from algorithms.resources import eng_alphabet

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def factory(s):
    global power
    result = ''
    for i in s:
        if i in eng_alphabet:
            if i == i.title():
                result += eng_alphabet[(eng_alphabet.index(i)+power) % 26].upper()
            else:
                result += eng_alphabet[(eng_alphabet.index(i)+power) % 26]
    if not result:
        result = '<Пусто>'
    return result

power = random.randint(1, 3)
#Если 0, то сдвиг вправо. Если 1, то сдвиг влево
if bool(random.getrandbits(1)):
    power = -power
