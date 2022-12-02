# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint

def input_list_random(n, lowlimit, highlimit):
    list = []
    for _ in range(n):
        list.append(randint(lowlimit, highlimit))
    print(f'Сформированный список:\n{list}')
    return list

def mult_number(list_number):
    mult =[]
    while len(list_number) > 1:
        mult.append(list_number[0] * list_number[-1])
        del list_number[0]
        del list_number[-1]
    if len(list_number) == 1:
        mult.append(list_number[0]**2)
    return print(f'Произведение пар чисел списка:\n{mult}')

len_list = int(input('Введите кол-во элементов в списке: '))
lowlimit = int(input('Введите нижнюю границу диапазона списка: '))
highlimit = int(input('Введите верхнюю границу диапазона списка: '))
input_list = input_list_random(len_list, lowlimit, highlimit)
mult_number(input_list)