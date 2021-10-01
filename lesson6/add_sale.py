import sys

summ = sys.argv[1]

with open("lesson6/bakery.csv", 'a', encoding='utf-8') as file:
    file.write(summ + '\n')
