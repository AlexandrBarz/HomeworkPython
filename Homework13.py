# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии. Не использовать функцию bin
import random

def number_random(lowlimit, highlimit):
    n = random.randint(lowlimit, highlimit)
    print(f'Введенное число:\n{n}')
    return n

# 1-й способ решения:
def conv_decimal_bin(n):
    bin_num = ''
    while n > 1:
        bin_num +=str(n % 2)
        n = n // 2
    else:
        bin_num += str(n % 2)
    return bin_num[::-1]

# 2-й способ решения:
def conv_recurse(n):
    if n == 0:
        return conv_number
    number = n % 2
    conv_number.append(number)
    conv_recurse(n // 2)
    return (''.join(map(str, conv_number[::-1])))

lowlimit = int(input('Введите нижнюю границу диапазона чисел: '))
highlimit = int(input('Введите верхнюю границу диапазона чисел: '))
n = number_random(lowlimit, highlimit)
print('\nИтог решения 1-ым способом:')
print(f'Перевод десятичного числа {n} в двоичную систему исчисления {conv_decimal_bin(n)}\n')
print('Итог решения 2-ым способом:')
conv_number = []
print(f'Перевод десятичного числа {n} в двоичную систему исчисления {conv_recurse(n)}\n')