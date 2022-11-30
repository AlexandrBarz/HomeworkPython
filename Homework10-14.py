# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


from random import randint

len_list = int(input('Введите кол-во элементов в списке: '))
list = []
for i in range(len_list):
    list.append(randint(0, 20))
print(f'Сформированный список:\n{list}')
sum = 0
for i in range(len_list):
    if (i % 2) == 1:
        sum += list[i]
print(sum)