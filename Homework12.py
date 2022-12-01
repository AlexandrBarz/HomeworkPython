# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random

def input_list_random(n, lowlimit, highlimit, number_sings):
    list = []
    for _ in range(n):
        list.append(round(random.uniform(lowlimit, highlimit), number_sings))
    print(f'Сформированный список:\n{list}')
    return list

def difference_max_min(input_list, number_sings):
    float_list =[]
    for i in range(len(input_list)):
        float_list.append(input_list[i] % 1)
        float_list[i] = round(float_list[i], number_sings)
    print(f'Сформированный список из дробной части чисел:\n{float_list}')
    max = float_list[0]
    min = float_list[0]
    for i in range(len(float_list)):
        if float_list[i] > max:
            max = float_list[i]
        if float_list[i] < min:
            min = float_list[i]
    difference = max - min
    return difference

len_list = int(input('Введите кол-во элементов в списке: '))
lowlimit = float(input('Введите нижнюю границу диапазона списка: '))
highlimit = float(input('Введите верхнюю границу диапазона списка: '))
number_sings = int(input('Введите кол-во знаков после запятой: '))
print(f'Разница между максимальным и минимальным значением дробной части:\n{difference_max_min(input_list_random(len_list, lowlimit, highlimit, number_sings), number_sings)}')