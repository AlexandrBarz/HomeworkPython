# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def number_check(input_string: str) -> int:
    """
    Функция проверяет корректность ввода

    Agrs:
    Intput_string  - ввод данных пользователя
    
    Return:
    int - натуральное число
    """
    while True:
        try:
            number = int(input(input_string))
            return number
        except ValueError:
            print('Некорректный ввод. Попробуйте снова')

def prime_factors(n: int) -> list:
    """
    Функция на вход принимает число и выдает список простых множителей

    Args:
    n  - целое число

    Return:
    list - список простых множителей введенного числа
    """
    i = 2
    primfact = []
    while i * i <= n:
        while not n % i:
            primfact.append(i)
            n = n / i
            i += 1
    if n > 1:
        primfact.append(n)
    return primfact

number = number_check('Введите натуральное число: ')
print(f'Список простых множителей числа {number}: {prime_factors(number)}')