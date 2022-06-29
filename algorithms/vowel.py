# Работает с латинским алфавитом
# Количество гласных в строке
import random
from algorithms.resources import eng_alphabet
from algorithms.resources import eng_vowels


def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))


def factory(s):
    result = 0
    for i in s:
        if i in eng_vowels:
            result += 1
    return str(result)
