import sys
import utils as util_cur                        # импортируем модуль созданный нами, как util_cur

ticker = sys.argv[1:]

util_cur.currency_rates(ticker[0])                  # запускаем функцию из нашего модуля несколько раз

