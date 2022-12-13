# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 (или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, лучше выделите в отдельные функции бота и умного бота

# 2 игрока 
from random import randint
candies = int(input('Сколько конфет: '))
take = int(input("Максимальное количество конфет можно взять: "))

def take_to_have_for_first(candies, take):
    take_candies = candies % (take + 1)
    if take_candies == 0:
        take_candies = take
    return(f'чтобы выиграть первому ходящему необходимо взять {take_candies}')
first_move = randint(1,2)
print(f"Первым ходит игрок {first_move}")
second_move = 3 - first_move
print(f'Второй ходит игрок {second_move}')
count = 0
while candies > 0:
    count += 1
    player1 = int(input("Ход первого игрока. Возьмите конфеты: "))
    candies = candies - player1
    print(f'осталось конфет: {candies}')
    print(take_to_have_for_first(candies, take))
    if candies > 0:
        player2 = int(input("Ход второго игрока. Возьмите конфеты: "))
        candies = candies - player2
        print(f'осталось конфет: {candies}')
        print(take_to_have_for_first(candies, take))
if candies == 0:
    print('Игра окончена')
if take % 2 != 0:
    print(f'Победил игрок {first_move}')
else:
    print(f'Победил игрок {second_move}')

# против бота

from random import *
import os
os.system("cls")

greeting = ('Вас приветствует игра "Забери все конфеты!"\n')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def candy(n):
    if n == 1 or n % 10 == 1:
        return 'а'
    elif 1 < n < 5 or 1 < n % 10 < 5:
        return 'ы'
    else:
        return ''


def acquaintance_players():
    player1 = input('Как Вас зовут? ')
    player2 = 'Алексей'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def rules(players):
    n = int(input('Сколько конфет будем разыгрывать? '))
    m = int(input('Сколько максимально будем брать конфет за один ход? '))     
    first = input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу ')
    if first != '1':
        first = 0
        return [n, m, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    print(count)

    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % (rules[1] + 1)
            if move == 0:
                move = rules[1]
            print(f'Я забираю {move} конфет{candy(move)}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{candy(rules[1])}, у нас всего {rules[0]} конфет{candy[rules[0]]}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{candy(rules[0])}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


print(greeting)

players = acquaintance_players()
rules = rules(players)

winer = play_game(rules, players, messages)
print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!\n')