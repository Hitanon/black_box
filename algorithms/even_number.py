#Количество четных чисел

import random

def get_random_string():
    return str(random.randint(100, 999))

def  factory(s):
    k = 0
    if s.isdigit():
        s = int(s)
        while s != 0:
            if s % 10 % 2 == 0:
                k +=1
            s = s // 10
    return str(k)

