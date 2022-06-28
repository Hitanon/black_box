# Если цифра четная, то (9-цифра), иначе цифра
import random

def get_random_string():
    return str(random.randint(100, 999))

def factory(x):
    result = ''
    if x.isdigit():
        x = int(x)
        while x:
            last = x % 10
            if last % 2 == 0:
                result = str(9 - last) + result
            else:
                result = str(last) + result
            x //= 10
    else:
        result = '<Пусто>'
    return result
