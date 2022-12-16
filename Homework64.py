# Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
url_list = ['https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod',
            'https://translate.google.ru/',
            'https://yandex.ru/search'            
            ]
domen_list = list(map(lambda i: i[:i.find('/')], [i for i in map(lambda i: i.replace('https://',''), url_list)]))
print(f'Список доменных имен:\n{domen_list}')