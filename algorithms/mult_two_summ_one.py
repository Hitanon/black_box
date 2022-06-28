# Умножить на 2 и прибаваляет 1

import random

def get_random_string():
    return str(random.randint(100, 999))

def factory(s):
    newnum = ''
    if s.isdigit():
        s = int(s)
        newnum = s * 2 + 1
    return str(newnum)
