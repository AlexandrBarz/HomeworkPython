# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д
from random import randint
import math
    
def input_list_random(n, lowlimit, highlimit):
    """
    Запрашивает кол-во элементов в списке и границы диапазона чисел, размещаемых в списке.
    Заполняет список случайными числами.
    
    Args:
    n - число элементов в списке
    lowlimit - граница нижнего диапазона случайных чисел
    highlimit - граница верхнего диапазона случайных чисел

    Return
    list - возвращает список из чисел с установленными границами
    """
    list = []
    
    for _ in range(n):
        list.append(randint(lowlimit, highlimit))
    print(f'Сформированный список:\n{list}')
    return list

len_list = int(input('Введите кол-во элементов в списке: '))
lowlimit = int(input('Введите нижнюю границу диапазона списка: '))
highlimit = int(input('Введите верхнюю границу диапазона списка: '))
original_list = input_list_random(len_list, lowlimit, highlimit)
mult_list = list(map(lambda i: (original_list[i]*original_list[-(i+1)]), [i for i in range(math.ceil(len(original_list)/2))]))
print(f'Список произведения парных элементов -> {mult_list}')