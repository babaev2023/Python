# Модули и пакеты

# Любой файл, который вы создали - скрипт - это модуль

import wordforms
import language.ru

for n in [0, 1, 2, 5, 11, 21, 23, 111]:
    print(
        n,
        'кочер' + wordforms.ending(
            n,
            ['га',  # 1
             'ги',  # 2, 3, 4
             'ёг'   # 5+
            ]))


for n in [0, 1, 2, 5, 11, 21, 23, 111]:
    print(
        n,
        'кочер' + language.ru.ending(
            n,
            ['га',  # 1
             'ги',  # 2, 3, 4
             'ёг'   # 5+
            ]))
