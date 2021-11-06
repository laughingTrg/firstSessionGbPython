import random                                                                   # импортируем библиотеку

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]                          # создаем списки со словами для шуток
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_random(words, repeat = True):                                               # функция возвращает случайное слово из списка слов
    if repeat:                                                                      # если повтор разрешен, то просто выбираем слово из списка
        return words[random.randint(0, len(words)-1)]
    else:                                                                           # если повтор запрещен, то удаляем выбранное слово из списка
        return words.pop(random.randint(0, len(words)-1))

def get_jokes(count, repeat = True):                                            # функция генерирует шутки
    jokes = []                                                                  # создаем массив шуток
    for i in range(count):                                                      # проходим столько раз, сколько передано в функцию
        if len(nouns) and len(adverbs) and len(adjectives) > 0:                 # если в списках еще есть слова, пишем шутки
            joke = f'{get_random(nouns, repeat)} {get_random(adverbs, repeat)} {get_random(adjectives, repeat)}' # составляем шутку с помощью функции
            jokes.append(joke)                                                  # get_random и доабвляем в список шуток
        else:                                                                   # если в списках нет больше слов для шуток
            jokes.append('Шутки кончились!')                                    # выводим последнюю надпись "Шутки кончились"
            break                                                               # досрочно выходим из функции
    print(jokes)                                                                # выводим список шуток

get_jokes(8, False)


