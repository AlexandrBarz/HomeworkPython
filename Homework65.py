# Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.

import random

numbers = [random.randint(1, 100) for _ in range(200)]
print(f'Исходный список -> {numbers}')
print(f'Список без совпадений -> {list(filter(lambda x: x[0] != x[1], enumerate(numbers)))}')