# Регулярные выражения - формула текста


import re

def check(formula, txt):
    if re.fullmatch(formula, txt):
        print(txt, ' СООТВЕТСТВУЕТ ', formula)
    else:
        print(txt, ' не соответствует ', formula)

check('a', 'a')
check('b', 'a')
check('.', 'a')
check('.', 'u')
check('\.', 'u')
check('\.', '.')
check('\d', 'u')
check('\d', '9')

# диапазоны

check('[0-9]', '0')
check('[0-9]', '6')
check('[0-9]', '9')
check('[0-9]', 't')
check('[a-z]', 't')
check('[a-z]', '9')
check('[a-zA-Z]', 'G')
check('[а-я]', 'ё')
check('[а-яё]', 'ё')


check('[аяуюоёыиэе]', 'ё')


check('[А-Я][а-яё]+', 'Ира')
check('[А-Я][а-яё]+', 'Вера')
check('[А-Я][а-яё]+', 'лёша')

check('[а-я]+-?[а-я]+', 'куданибудь')
check('[а-я]+-?[а-я]+', 'куда-нибудь')

# 1. Показать, что плюсик - лишний символ

vyraj = '='
check(vyraj + vyraj + '*', '=======')

uzor = '=^.^='
check('(%s)*' % uzor.replace('^', '\\^'), uzor*10)

# Указываем количество повторов:

phone = "+79161234567"
formula = '\+[0-9]{5,11}'
check(formula, phone)


# | Этот значок дает возможность выбора одного из вариантов

phone = "+7(916)123 4567"
formula = '\+[0-9](\([0-9]{3}\)|[0-9]{3})[0-9]{3} ?[0-9]{4}'
check(formula, phone)

check('\+\d{1}\D?\d{3}\D?\d{3}\D?\d{2}\D?\d{2}','+7(915]435 43 21')
