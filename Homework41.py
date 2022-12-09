# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(n):
    primfact = []
    while i * i <= n:
        while not n % i:
            primfact.append(i)
            n = n / i
            i += 1
    if n > 1:
        primfact.append(n)
    return primfact

# number = number_check('Введите натуральное число: ')
number = int(input('Введите натуральное число: '))
print(f'Список простых множителей числа {number}: {prime_factors(number)}')