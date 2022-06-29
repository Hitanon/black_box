#Количество четных чисел в ненулевом числе

import random

def get_random_string():
    return str(random.randint(100, 999))

def  factory(s):
    k = 0
    flag = True
    for i in s:
        if not(i.isdigit() or i == '-'):
            flag = False
    if flag:
        s = abs(int(s))
        while s != 0:
            if s % 10 % 2 == 0:
                k += 1
            s = s // 10
    return str(k)


