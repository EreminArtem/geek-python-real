import sys

args = sys.argv[1:]
try:
    start = int(args[0])
except IndexError:
    start = None
try:
    end = int(args[1])
except IndexError:
    end = None

with open("lesson6/bakery.csv", 'r', encoding='utf-8') as file:
    for number, line in enumerate(file):
        if start is not None and start > number + 1:
            continue
        if end is not None and end < number + 1:
            break
        print(line, end='')
