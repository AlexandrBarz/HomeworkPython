# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
import random
n = input('Введите размер массива: ')
if n.isdigit() == True:
    numbers = []
    for i in range(int(n)):
        numbers.append(random.randint(-100, 100))
    print(f'Исходный массив:\n{numbers}')
    new_numbers = numbers.copy()
    count = 0
    for x in range(len(numbers)):
        if numbers[x] < 0:
            count += 1
            new_numbers.insert(x+count, '0')
    print(f'Итоговый массив:\n{new_numbers}')
else:
    print('Вместо числа был введен символ. Попробуйте еще раз.')