# Из списка Homework65 оставьте только те пары, где сумма кортежа кратна 5
import random

numbers = [random.randint(1, 100) for _ in range(20)]
print(f'Исходный список -> {numbers}')
print(f'Список пар, где сумма кортежа кратна 5 -> {list(filter(lambda x: (x[0]+x[1])%5==0, enumerate(numbers)))}')