# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N. Не используйте функцию math.factorial.
n = input('Введите число: ')
if n.isdigit() == True:
    n = int(n)
    row = list(range(1, n+1))
    print(f'Набор заданных чисел от 1 до {n}:\n{row}')
    factorial = 1
    res = []
    for i in row:
        factorial *= i
        res.append(factorial)
    print(f'Набор произведений чисел от 1 до {n} (факториал):\n{res}')
else:
    print('Вместо числа был введен символ. Попробуйте еще раз.')
