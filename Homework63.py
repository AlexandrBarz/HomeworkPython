# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

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

print([((-3)**i) for i in range(number_check('Введите число членов последовательности: '))])