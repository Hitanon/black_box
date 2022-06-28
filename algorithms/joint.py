# Общие буквы из англиского и русского алфавитов
import random
from algorithms.resources import eng_alphabet
from algorithms.resources import joint_alphabet


def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))


def factory(s):
    result = ''
    for i in s:
        if i in joint_alphabet:
            result += i
    if not result:
        result = '<Пусто>'
    return result
