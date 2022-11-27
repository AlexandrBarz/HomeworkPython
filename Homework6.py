# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Метод через строковую переменную
# num = input('Введите число: ')
# sum = 0
# for i in num:
#     if (i != '.') and (i !=','):
#         sum += int(i)
# print(f'Сумма цифр введенного числа {num} = {sum}')


# Метод через переменную float
def sum_digit (x):
    sum = 0
    while x > 0:
        res = x % 10
        sum += res
        x //= 10
    return sum

number = input('Введите число: ')
number1 = abs(float(number))
number2 = number1 - math.floor(number)
number1 == math.floor(number)

print(f'Сумма цифр введенного числа {number} = {sum_digit(number1)}')