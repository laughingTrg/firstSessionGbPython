def num_translate(number):                          # создали функцию, которая возвращает соответствие английского числа русскому
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if number == number.capitalize():               # если значение с большой буквы, то вывод делаем с большой буквы
        res = (numbers.get(number.lower(), None)).capitalize()
    else:
        res = numbers.get(number, None)             # если числа нет, то возвращается значение по умолчанию
    return res

print(num_translate('five'))
print(num_translate('Ten'))
print(num_translate('twenty'))