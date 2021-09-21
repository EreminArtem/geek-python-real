from datetime import datetime
from decimal import Decimal

import requests as requests
from requests import utils


def currency_rates(code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    currency_index = content.find(code.upper())
    if currency_index == -1:
        return None
    start_rate_index = content.find('Value>', currency_index) + len('Value>')
    end_rate_index = content.find('<', start_rate_index)
    # не знаю какой вариант лучше, если честно. По поводу того что лучше возвращать, это тоже не знаюб зависит от
    # того что мы потом будем с этим делать. Пока возвращаю пару, а там уже смотреть надо.
    return get_currency_date(content), Decimal(content[start_rate_index:end_rate_index].replace(',', '.'))
    # return (
    #     get_currency_date(content),
    #     Decimal(
    #         next(
    #             filter(lambda s: s.find(code.upper()) != -1, content.split('ID'))
    #         ).split('Value')[1][1:-2].replace(',', '.')
    #     )
    # )


def get_currency_date(content):
    date_index = content.find('Date="') + len('Date=') + 1
    return datetime.strptime(content[date_index: content.find('"', date_index)], '%d.%m.%Y')

