"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:

>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""
import re
from functools import wraps


def email_parse(email_address: str):
    email_parser = re.compile('^(.+)@(.+\.[a-z]{2,})')
    if not email_parser.match(email_address):
        raise ValueError

    passed_email = email_parser.findall(email_address)
    return {'username': passed_email[0][0], 'domain': passed_email[0][1]}


# print(email_parse('someone@geekbrains.ru'))

"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? 
Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? 
Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


# не понял зачем мне тут маскирование
def type_logger(func):
    def wrapper(*args, **kwargs):
        _args = []
        for arg in args + tuple(kwargs.values()):
            _args.append(f'{arg}: {type(arg)}')
        print(f'{func.__name__}({", ".join(_args)})')
        result = func(*args, **kwargs)
        print(type(result))
        return result

    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** 3


# print(calc_cube(3, 5))

"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать 
исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(predicate):
    def _val_checker(func):
        @wraps(func)  ## не совсем понял зачем мне здесь это
        def wrapper(*args, **kwargs):
            for arg in args + tuple(kwargs.values()):
                if not predicate(arg):
                    raise ValueError
            return func(*args, **kwargs)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube2(x):
    return x ** 3


print(calc_cube2(2))
