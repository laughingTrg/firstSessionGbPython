import utils as util_cur                        # импортируем модуль созданный нами, как util_cur

util_cur.currency_rates('USD')                  # запускаем функцию из нашего модуля несколько раз
util_cur.currency_rates('gbp')                  # убеждаемся, что ничего лишнего не выполняется и в консоль не падает
util_cur.currency_rates('Eur')
