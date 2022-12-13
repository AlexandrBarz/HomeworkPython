# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
del_word = input('Введите слово, которое хотите удалить: ')
string = input('Введите строку: ')
split_string = string.split()
filter_string = ' '.join(filter(lambda s: del_word not in s, split_string))
print('Отфильтрованная строка:', filter_string)