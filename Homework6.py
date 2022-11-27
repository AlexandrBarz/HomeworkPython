# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# num = input('Введите число: ')
# #if num.startswith('-') or num.isdigit():
# sum = 0
# for i in num:
#     if (i != '.') and (i !=','):
#         sum += int(i)
# print(f'Сумма цифр введенного числа {num} = {sum}')
# # else:
#     # print('Необходимо ввести число вместо символа')

num = float(input('Введите число: '))
num1 = abs(num)
sum = 0
while num1 > 0:
    res = num1 % 10
    sum += res
    num1 //= 10
    print(num1)
print(f'Сумма цифр введенного числа {num} = {sum}')