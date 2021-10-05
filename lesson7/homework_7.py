import json
import os
import shutil
from pprint import pprint

import yaml

"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, 
его можно создать в любом текстовом редакторе «руками» (не программно); 
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""


def create_starter():
    global config
    with open("config.yaml", 'r', encoding='utf-8') as config_stream:
        config = yaml.safe_load(config_stream)
        pprint(config)
    creator(config)


def creator(element):
    if type(element) == dict:
        for key, value in element.items():
            create_dir(key)
            os.chdir(key)
            creator(value)
            os.chdir('../')
    elif type(element) == list:
        for el in element:
            creator(el)
    else:
        create_file(element)


def create_dir(key):
    if not os.path.exists(key):
        os.mkdir(key)


def create_file(file_name):
    with open(file_name, 'w') as f:
        pass


# create_starter()

"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, 
что html-файлы расположены в родительских папках (они играют роль пространств имён); 
предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
"""
templates = 'templates'


def move_templates(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                dst = os.path.join(os.getcwd(), 'my_project', templates, os.path.basename(root))
                if not os.path.exists(dst):
                    os.makedirs(dst)
                shutil.copyfile(file_path, os.path.join(dst, file))

        for d in dirs:
            move_templates(d)


# move_templates('my_project')


"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, 
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""


def create_static(dir_path, result_dict: dict):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            key = rounder(os.stat(os.path.join(root, file)).st_size)
            res = result_dict.setdefault(key, (0, []))
            count = res[0] + 1
            exts = res[1]
            if ext not in res[1]:
                exts.append(ext)
            result_dict[key] = (count, exts)
        for d in dirs:
            create_static(d, result_dict)
    return result_dict


def rounder(n):
    return n - n % 1000


with open("statistics.json", "w") as stream:
    json.dump(create_static('some_data', {}), stream)
