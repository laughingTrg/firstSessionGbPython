import re

txt = 'someone@geekbrains.ru'                                                           # создаем строки для теста скрипта
txt2 = 'someone@geekbrainsru'
txt3 = 'someonegeekbrains.ru'

def email_parse(email_adr):
    RE_USER_DOMAIN = re.compile(r'(?P<user>[^&]+)@(?P<domain>[^&]+)')                   # получаем из регулярки словарик и данные
    msg = f'wrong email: {email_adr}'                                                   # задаем сообщение для вывода ошибки
    if not RE_USER_DOMAIN.match(email_adr):                                             # если адрес не совпадает, например, нет @
        raise ValueError(msg)                                                           # вызываем исключение ValueError с сообщением
    elif RE_USER_DOMAIN.findall(email_adr)[0][-1].find('.') == -1:                      # если домен не подходит выводим ошибку
        msg = f'wrong email: {email_adr}'
        raise ValueError(msg)                                                           # вызываем исключение ValueError с сообщением
    print(*map(lambda x: x.groupdict(), RE_USER_DOMAIN.finditer(email_adr)), sep=', ')  # выводим согласно заданию

email_parse(txt)
email_parse(txt2)
email_parse(txt3)