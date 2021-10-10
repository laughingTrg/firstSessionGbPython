prices = [57.8, 46.51, 97, 31.02, 154.3, 953.06, 73.4, 15.9, 9.45, 17.88]   # исходный список цен на товары

print('Выводим список цен в заданном формате: ', end=' ')
for price in prices:                                                            # проходим по списку для разделения элементов и вывода отдельно руб и коп
    str_price = str(price)
    if price != prices[len(prices) - 1]:                                        # если элемент списка не последний то делаем вывод как написано ниже
        if len(str_price.split('.')) > 1:                                       # если копейки есть выполняется 1 часть кода
            if len(str(price).split(".")[1]) == 1:                              # если разрядность копеек равна 1 выводим таким образом
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1])*10} коп', end=', ')
            else:
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1]):02d} коп', end=', ')
        else:                                                                   # если копеек нет, выполняем эту часть
            print(f'{price:02d} руб 00 коп', end=', ')
    else:                                                                               # если последний элемент нужно в конце перевести коретку и убрать запятую
        if len(str_price.split('.')) > 1:                                               # если копейки есть выполняется
            if len(str(price).split(".")[1]) == 1:                                      # если разрядность копеек равна 1 выводим таким образом
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1]) * 10} коп')
            else:
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1]):02d} коп')
        else:                                                                           # если копеек нет, выполняем эту часть
            print(f'{price:02d} руб 00 коп')
print('--------------------')
print('Выводим сортированный список цен по возрастанию в заданном формате: ', end=' ')
for price in sorted(prices):                                                # выводим цены отсортированные по возрастанию новый список не создаем
    str_price = str(price)
    if price != sorted(prices)[len(prices) - 1]:                            # если элемент списка не последний то делаем вывод как написано ниже
        if len(str_price.split('.')) > 1:                                   # проверяем наличие копеек и количество символов
            if len(str(price).split(".")[1]) == 1:
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1])*10} коп', end=', ')
            else:
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1]):02d} коп', end=', ')
        else:
            print(f'{price:02d} руб 00 коп', end=', ')
    else:                                                                   # если последний элемент нужно в конце перевести коретку и убрать запятую
        if len(str_price.split('.')) > 1:
            if len(str(price).split(".")[1]) == 1:
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1])*10} коп')
            else:
                print(f'{int(str(price).split(".")[0]):02d} руб {int(str(price).split(".")[1]):02d} коп')
        else:
            print(f'{price:02d} руб 00 коп')
print('--------------------')
print('Проверка неизменности исходного списка цен: ', prices)               # выводим оригинальный список, доказываем, что он не изменился
print('--------------------')
high_to_low = prices.copy()                                                 # создаем копию списка, не изменяя исходный
high_to_low.sort(reverse=True)                                              # сортируем новый список по убыванию
print('Выводим копию исходного списка сортированного по убыванию: ', high_to_low)     # выводим отсортированный список
print('--------------------')
print(f'Цены пяти самых дорогих товаров: ', end='')                         # выводим список пяти самых дорогих товаров
for item in high_to_low[:5]:                                                # идем по срезу через цикл
    if item != high_to_low[4]:
        if float(item).is_integer():
            print(f'{item} руб 00 коп, ', end='')
        else:
            if len(str(item).split(".")[1]) < 2:
                print(f'{int(str(item).split(".")[0]):02d} руб {int(str(item).split(".")[1] + "0")} коп, ', end='')
            else:
                print(f'{int(str(item).split(".")[0]):02d} руб {int(str(item).split(".")[1]):02d} коп, ', end='')
    else:
        if float(item).is_integer():
            print(f'{item} руб 00 коп ')
        else:
            if len(str(item).split(".")[1]) < 2:
                print(f'{int(str(item).split(".")[0]):02d} руб {int(str(item).split(".")[1] + "0")} коп ')
            else:
                print(f'{int(str(item).split(".")[0]):02d} руб {int(str(item).split(".")[1]):02d} коп ')