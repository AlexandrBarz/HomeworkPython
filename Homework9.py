# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из тех, кто участвовал в этом счете, получил по одной монете,
# остальные получили по две монеты. Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру. 
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep. Определите номер этого человека и количество монет, которые оказались у него в конце игры.

n = int(input('Кол-во человек:'))
m = int(input('Кол-во человек, которое посчитал ведущий: '))
last = 0
for i in range(1, n + 1):
    last = (last + m) % i
    print(last)
print(last + 1)