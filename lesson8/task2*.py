import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as logs:                     # открываем файл и парсим посрочно в список необходимые данные
    RE_PARSE_LOGS = re.compile(r'^(?P<ip>(?:\d*.){3}\d*).+\[(?P<time>[^&]+)(?=]).{3}(?P<type>[^ \"]+)\ (?P<path>[^\ ]+).+(?<=\"\ )(?P<code>[^ \"]+)\s(?P<size>[^ ]+)')
    for line in logs:
        print(*RE_PARSE_LOGS.findall(logs.readline()))
