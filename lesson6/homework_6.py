"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""
import sys
from itertools import zip_longest


def get_spamer_ip():
    logs_by_ip = {}
    with open("nginx_logs.txt", "r", encoding='utf-8') as log:
        for i in log:
            line = i.split()
            logs_by_ip.setdefault(line[0], []).append((line[5][1:], line[6]))
    return max(logs_by_ip.keys(), key=lambda x: len(x[1]))


# print(get_spamer_ip())


"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. 
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. 
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». 
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""


def users_hobby():
    with open('users.csv', 'r', encoding='utf-8') as users_stream:
        users = users_stream.read().replace(',', ' ').split('\n')
        with open('hobby.csv', 'r', encoding='utf-8') as hobbies_stream:
            hobbies = hobbies_stream.read().split('\n')
            if len(users) < len(hobbies):
                sys.exit(1)
            hobby_by_user = zip_longest(users, hobbies)
            with open('users_hobby.txt', 'w', encoding='utf-8') as users_hobbies:
                print(dict(hobby_by_user), file=users_hobbies)


# users_hobby()


"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ 
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей 
и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). 
Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, 
полученные в результате парсинга.
"""


def users_hobby_by_line():
    with open('users.csv', 'r', encoding='utf-8') as users_stream:
        hobby_by_user = {}
        with open('hobby.csv', 'r', encoding='utf-8') as hobbies_stream:
            for user in users_stream:
                hobby = hobbies_stream.readline().replace('\n', '')
                hobby = hobby if hobby else None
                hobby_by_user.setdefault(user.replace(',', ' ').replace('\n', ''), set()).add(hobby)
            if hobbies_stream.readline():
                sys.exit(1)
        with open('users_hobby.txt', 'w', encoding='utf-8') as users_hobbies:
            print(dict(hobby_by_user), file=users_hobbies)

# users_hobby_by_line()
