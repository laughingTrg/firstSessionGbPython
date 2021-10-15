def thesaurus(names):
    char_name = {}                                                              # создаем пустой словарь
    for name in names:                                                          # проходим по все элементам списка имен и фамилий
        first_char_name = name.split(' ')[0][0]                                 # получаем первую букву имени
        char_name[first_char_name] = list(filter(lambda x: x.split(' ')[0][0] == first_char_name, names))     # если они удовлетворяют условию (первая буква имени одинаковая)
    return char_name                                                            # создаем словарь, в котором ключ - первая буква схожих имен, а значение список фамилий и имен


def thesaurus_adv(*surenames):                                                  # функция принимает имена фамилии и организует словарь где ключ
    char_surename = {}                                                          # первая буква фамилии, а значение словарь из функции "thesaurus"
    list_keys = []                                                              # создаем пустой список для хранения ключей
    for surename in sorted(surenames):                                          # проходим по всем эдементам, передаваемым в функцию
        if surename.split(' ')[1][0] not in list_keys:                          # если ключа (1 буква фамилии) нет в списке - добавляем
            list_keys.append(surename.split(' ')[1][0])
    list_keys = sorted(list_keys)                                               # сортируем полученный список
    for key in list_keys:                                                       # наполняем выходной словарь ключами с значениями None
        char_surename[key] = None
    for surename in sorted(surenames):                                                  # проходим по всем эдементам, передаваемым в функцию
        first_char = surename.split(' ')[1][0]                                  # определяем 1 букву фамилии
        char_surename[first_char] = thesaurus(list(filter(lambda x: x.split(' ')[1][0] == first_char, sorted(surenames))))  #присваиваем ключ - первая буква фамилии
    return print(char_surename)                                                 # значение словарь, как результат функции "thesaurus", lambda сравнивает 1 букву фамилии

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

