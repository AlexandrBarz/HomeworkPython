# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint

def input_list_random(n, lowlimit, highlimit):
    list = []
    for _ in range(n):
        list.append(randint(lowlimit, highlimit))
    print(f'Сформированный список:\n{list}')
    return list

# 1-й способ решения:
def summa_number(len_list, list_number):
    summa = 0
    for i in range(len_list):
        if (i % 2) == 1:
            summa += list_number[i]
    return print(f'Сумма элементов списка, стоящих на нечетных позициях:\t{summa}\n')

# 2-й способ решения:
def sum_number(list_number):
    return print(f'Сумма элементов списка, стоящих на нечетных позициях:\t{sum(list_number[1::2])}\n')

len_list = int(input('Введите кол-во элементов в списке: '))
lowlimit = int(input('Введите нижнюю границу диапазона списка: '))
highlimit = int(input('Введите верхнюю границу диапазона списка: '))
input_list = input_list_random(len_list, lowlimit, highlimit)
print('\nИтог решения 1-ым способом:')
summa_number(len_list, input_list)
print('Итог решения 2-ым способом:')
sum_number(input_list)