# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def number_check(input_string: str) -> int:
    """
    Функция запрашивает ввод и проверяет введенные данные на корректность

    Args:
    input_string - предлогает пользователю ввести данные 

    Return:
    int - возвращает целое число
    """
    while True:
        try:
            number = int(input(input_string))
            return number
        except ValueError:
            print('Некорректный ввод. Попробуйте снова')
    
def prime_factors(n: int) -> list:
    """
    Функция выводит список простых множителей числа

    Args:
    n - принимает на вход число 

    Return:
    list - возвращает список простых множителей числа
    """
    i = 2
    primfact = []
    while i * i <= n:
        while n % i == 0:
            primfact.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfact.append(n)
    return primfact

number = number_check('Введите натуральное число: ')
print(f'Список простых множителей числа {number} ---> {prime_factors(number)}')