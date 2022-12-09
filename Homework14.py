# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibo_num(n):
    fibo_num =[]
    fib1, fib2 = 1, 1
    for i in range(n):
        fibo_num.append(fib1)
        fib1, fib2 = fib2, fib1 + fib2
    fib1, fib2 = 0, 1
    for i in range(n + 1):
        fibo_num.insert(0, fib1)
        fib1, fib2 = fib2, fib1 - fib2
    return fibo_num
    
n = int(input('Введите число: '))
fibo_nums = fibo_num(n)
print(f'Список из чисел Фибоначчи для числа {n}:\n{fibo_nums}')