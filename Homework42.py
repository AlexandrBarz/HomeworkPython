# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
def non_repeating_elements(spisok):
    """
    Функция выдает список неповторяющихся элементов последовательности

    Args:
    spisok - принимает на вход список чисел

    Return:
    new_spisok - возвращает отсортированный список неповторяющихся элементов последовательности
    """
    new_spisok = []
    [new_spisok.append(i) for i in spisok if i not in new_spisok]
    new_spisok.sort()
    return new_spisok

spisok = list(map(int, input('Ввведите числа через пробел: ').split()))
print(f'Список неповторяющихся элементов последовательности {spisok} ---> {non_repeating_elements(spisok)}')