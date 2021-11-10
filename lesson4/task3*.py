import requests                                                                 # импорт библиотеки requests
from decimal import Decimal                                                     # импорт библиотеки для работы с типом Decimal
import datetime

def get_info(teg_start, teg_end, http_str):                                     # функция возвращает float значение из html между указанными тегами
    return float('.'.join(http_str[http_str.find(teg_start) + len(teg_start): http_str.find(teg_end)].split(',')))

def get_info_dec(teg_start, teg_end, http_str):                                 # функция возвращает decimal значение из html между указанными тегами
    return Decimal('.'.join(http_str[http_str.find(teg_start) + len(teg_start): http_str.find(teg_end)].split(',')))

def currency_rates(ticker):                                                     # функция принимает тикер валюты и возвращает ее стоимость к рублю
    responce = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')          # получаем html страницу в текст
    if responce.text.find(ticker.upper()) == -1: return print(None)             # если заданного тикера нет в строке, возвращаем None
    get_date_info = (responce.text.split('Date="')[1][:10]).split('.')          # получаем дату из ответа сервера
    currency_date = datetime.date(year=int(get_date_info[-1]), month=int(get_date_info[1]), day=int(get_date_info[0]))  # заносим дату в формат datetime
    get_ticker_info = responce.text.split(ticker.upper())                       # иначе разделяем строку по имени тикера
    get_ticker_info = get_ticker_info[1].split('</Valute>')                     # отрезаем остальную часть строки оставляя только информацию с тикером
    nominal = get_info_dec('<Nominal>', '</Nominal>', get_ticker_info[0])       # отпределяем значение номинала либо в float, либо в Decimal
    value = get_info_dec('<Value>', '</Value>', get_ticker_info[0])             # отпределяем значение стоимости либо в float, либо в Decimal
    return print(f'currency {ticker.upper()} to RUB: {value/nominal}, {currency_date}')                  # выводим строку ответа

currency_rates('usd')
currency_rates('EUr')
currency_rates('GBP')
