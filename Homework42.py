# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
def non_repeating_elements(spisok):
    new_spisok = []
    [new_spisok.append(i) for i in spisok if i not in new_spisok]
    return new_spisok

spisok = list(map(int, input('Ввведите числа через пробел: ').split()))
print(f'Список неповторяющихся элементов последовательности {spisok} ---> {non_repeating_elements(spisok)}')