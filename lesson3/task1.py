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
    return numbers.get(number, None)                # если числа нет, то возвращается значение по умолчанию

print(num_translate('five'))
print(num_translate('ten'))
print(num_translate('twenty'))
