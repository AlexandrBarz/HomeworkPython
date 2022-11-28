# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
import random
n = int(input('Введите размер массива: '))
numbers = []
for i in range(n):
    numbers.append(random.randint(-100,100))
print(f'Исходный массив:\n{numbers}')
new_numbers = numbers.copy()
count = -1
for x in range(len(numbers)):
    if numbers[x] < 0:
        count +=1
        new_numbers.insert(x+1+count,'0')
print(f'Итоговый массив:\n{new_numbers}')