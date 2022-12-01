# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

def input_list_random(n, lowlimit, highlimit):
    list = []
    for i in range(n):
        list.append(randint(lowlimit, highlimit))
    print(f'Сформированный список:\n{list}')
    return list

len_list = int(input('Введите кол-во элементов в списке: '))
lowlimit = int(input('Введите нижнюю границу диапазона списка: '))
highlimit = int(input('Введите верхнюю границу диапазона списка: '))
input_list = input_list_random(len_list, lowlimit, highlimit)

#  # 1-й способ решения:
summa = 0
for i in range(len_list):
    if (i % 2) == 1:
        summa += input_list[i]
print(summa)

# 2-й способ решения:
print(sum(input_list[1::2]))