# Находит сумму цифр

import random

def get_random_string():
    return str(random.randint(100, 999))

def  factory(s):
    sum = 0
    if s.isdigit():
        s = int(s)
        while s != 0:
            sum += s % 10
            s = s // 10
    return str(sum)
