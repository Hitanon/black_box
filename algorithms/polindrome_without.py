#Полиндром без согласных/гласных
import random
from algorithms.resources import eng_alphabet
from algorithms.resources import eng_vowels
from algorithms.resources import eng_consonant

def get_random_string():
    return ''.join(random.choice(eng_alphabet) for i in range(random.choice((3, 4))))

def factory(s):
    global isVowel
    result = ''
    if isVowel:
        #Без гласных
        for i in s:
            if i in eng_consonant:
                result += i
    else:
        #Без согласных
        for i in s:
            if i in eng_vowels:
                result += i
    if not result:
        result = '>отсуП<'
    return result[::-1]

isVowel = bool(random.randbytes(1))
