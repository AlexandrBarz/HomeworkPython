# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Back.BLUE + 'Игра крестики-нолики' + Style.RESET_ALL)

field = list(range(1,10))

def draw_field(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input(Fore.GREEN + "Куда поставим " + Fore.BLUE + player_token + Style.RESET_ALL + Fore.GREEN + "? " + Style.RESET_ALL)
      try:
         player_answer = int(player_answer)
      except:
         print(Fore.RED + "Некорректный ввод. Вы уверены, что ввели число?" + Style.RESET_ALL)
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(field[player_answer-1]) not in "XO"):
            field[player_answer-1] = player_token
            valid = True
         else:
            print(Fore.YELLOW + "Эта клетка уже занята!" + Style.RESET_ALL)
      else:
        print(Fore.RED + "Некорректный ввод. Введите число от 1 до 9." + Style.RESET_ALL)

def check_win(field):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False

def main(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(field)
           if tmp:
              print(Fore.CYAN + tmp, Fore.CYAN + "Вы выиграли!" + Style.RESET_ALL)
              win = True
              break
        if counter == 9:
            print(Fore.YELLOW + "Ничья!" + Style.RESET_ALL)
            break
    draw_field(field)
main(field)