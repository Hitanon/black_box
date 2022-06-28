# Если буква Заглавная, то меняется на строчную и смещается на 1 влево в алфавите
# Если буква строчная, то меняется на Заглавную и смещается на 1 вправо в алфавите
import random
from algorithms.resources import eng_alphabet


def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))


def factory(s):
    result = ''
    for i in s:
        if i in eng_alphabet:
            if i == i.title():
                result += eng_alphabet[(eng_alphabet.index(i) - 1) % 26]
            else:
                result += eng_alphabet[(eng_alphabet.index(i) + 1) % 26].upper()
    if not result:
        result = '<Пусто>'
    return result
