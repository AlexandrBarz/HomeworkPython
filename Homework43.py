# В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».Нужно перезаписать файл.
def uppercase(student, value):
    spisok = ''
    for name in student:
        if name.count(value):
            name = name.upper()
        string = name + '\n'
        spisok += string
    return spisok

spisok = open('File43.txt', 'r', encoding='utf-8')
str_spisok = spisok.read().split('\n')
spisok.close()

new_spisok = uppercase(str_spisok, value ='5')

spisok = open('File43.txt', 'w', encoding='utf-8')
spisok.write(new_spisok)
spisok.close()