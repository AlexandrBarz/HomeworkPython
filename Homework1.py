# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# ***Дополнительно**: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон.
day_week = input('Введите день недели: ')
if day_week.startswith('-'):
    print(f'Введенное число {day_week} - не соотвествует дню недели. Попробуйте еще раз')
elif day_week.isdigit() == True:
    day_week = int(day_week)
    if (day_week == 6) or (day_week == 7):
        print(f'{day_week} - выходной день')
    elif (day_week < 1) or (day_week > 7):
        print(f'Введенное число {day_week} - не соотвествует дню недели. Попробуйте еще раз')
    else:
        print(f'{day_week} - рабочий день')
else:
    print('Необходимо ввести число вместо символа')