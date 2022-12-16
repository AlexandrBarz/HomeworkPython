# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# ["qwe", "asd", "zxc", "qwe", "ertqwe"],  "qwe", ответ: 3
# ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# ["123", "234", 123, "567"], ищем: "123", ответ: -1

def find_second_occurence(string_list, find_word):
    try:
        list_indexes = [index for index, string in enumerate(string_list) if string == find_word]
        return list_indexes[1]
    except IndexError:
        return print('Вхождение строки в список либо отсутствует полностью, либо отсутствует второе вхождение')

original_string = (input('Введите строку: ')).split()
find_word = input('Введите строку: ')
print(find_second_occurence(original_string, find_word))