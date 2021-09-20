"""
1. Написать функцию num_translate(),
переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
"""
import random


def num_translate(num_string):
    # если хранить снаружи, то функция получается чистая
    # если словарь изменится можем быть уверены что нигде ничего не сломается кроме как здесь
    # с другой стороны он будет создаваться каждый раз при вызове функции,
    # так что оптимизированнее создать константу один раз
    # Не знаю как лучше пока классы и импорт из файла не проходили, зависит от ситуации
    nums = {"zero": "ноль", "one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять",
            "six": "шесть", "seven": "семь",
            "eight": "восемь", "nine": "девять", "ten": "десять"}
    return nums.get(num_string)


# print(num_translate("one"))
# print(num_translate("noop"))

"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, 
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""


def num_translate_adv(num_string: str):
    if num_string.islower():
        return num_translate(num_string.lower())
    else:
        return num_translate(num_string.lower()).capitalize()


# print(num_translate_adv("One"))
# print(num_translate_adv("two"))


"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки?
Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
"""


def thesaurus(*names):
    names_dict = {}
    for i in names:
        names_dict.setdefault(i[0], []).append(i)
    return names_dict


def thesaurus_adv(*names):
    names_dict = {}
    for i in names:
        name_dict = thesaurus(i).popitem()
        names_dict.setdefault(i.split()[1][0], {}).setdefault(name_dict[0], []).append(name_dict[1][0])
    return names_dict


def sort_dict(dictionary: dict):
    result = []
    for i in sorted(dictionary.keys()):
        result.append(dictionary[i])
    return result


# print(thesaurus("Иван", "Мария", "Петр", "Илья"))
# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформир`ованных из трех случайных слов, 
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, 
разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? 
Сможете ли вы сделать аргументы именованными?
"""


def get_jokes(count: int, unique: bool):
    """
    Создаёт шутки
    :param unique: флаг уникальности слов в шутках, если выставлен в True, то count не может быть больше 5
    :param count: кол-во шуток
    :return: массив с шутками
    """
    if unique and count > 5:
        return

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    result = []
    for i in range(count):
        rand = random.randint(0, len(nouns) - 1)
        if unique:
            joke = f"{nouns.pop(rand)} {adverbs.pop(rand)} {adjectives.pop(rand)}"
        else:
            joke = f"{nouns[rand]} {adverbs[rand]} {adjectives[rand]}"

        result.append(joke)

    return result


print(get_jokes(count=5, unique=True))
