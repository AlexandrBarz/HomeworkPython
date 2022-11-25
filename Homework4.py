# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
import math
quarter = input('Введите номер координатной четверти: ')
if (quarter.isdigit() == True):
    quarter = int(quarter)
    while (quarter < 5):
        x_pos_end = math.inf
        y_pos_end = math.inf
        x_neg_end = -math.inf
        y_neg_end = -math.inf
        if (quarter == 1):
            print(f'Диапазон возможных координат точки в 1-й четверти:\nx = {(0, x_pos_end)} и y = {(0, y_pos_end)}')
            break
        elif (quarter == 2):
            print(f'Диапазон возможных координат точки во 2-й четверти:\nx = {(0, x_neg_end)} и y = {(0, y_pos_end)}')
            break
        elif (quarter == 3):
            print(f'Диапазон возможных координат точки в 3-й четверти:\nx = {(0, x_neg_end)} и y = {(0, y_neg_end)}')
            break
        elif (quarter == 4):
            print(f'Диапазон возможных координат точки в 4-й четверти:\nx = {(0, x_pos_end)} и y = {(0, y_neg_end)}')
            break
    else:
        print(f'Четверти {quarter} не существует.')
else:
    print('Необходимо ввести число вместо символа')