# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
import math

def input_list_random(n, lowlimit, highlimit):
    list = []
    for i in range(n):
        list.append(randint(lowlimit, highlimit))
    print(f'Сформированный список:\n{list}')
    return list

def mult(list_number):
    mult =[]
    while len(list_number) > 1:
        mult.append(list_number[0] * list_number[-1])
        del list_number[0]
        del list_number[-1]
    else:
        mult.append(list_number[0]**2)
    return print(mult)

len_list = int(input('Введите кол-во элементов в списке: '))
lowlimit = int(input('Введите нижнюю границу диапазона списка: '))
highlimit = int(input('Введите верхнюю границу диапазона списка: '))
input_list = (input_list_random(len_list, lowlimit, highlimit))
mult(input_list)