﻿"""
#Day_3\Work2.py
Задача №2

Вход:
расстояние (100 - 10000 включительно)
расход в литрах на 100 км(5 - 25) и
стоимость бензина (45 - 55).
входные данные - это целые или дробные числа.

Выход: Проверить входные данные поездки и если данные верные - посчитать стоимость поездки, вывести ее на экран. 
В противном случае, вывести сообщение о том, что данные некорректны.
"""

distance = float(input('Ввести асстояние от 100 - 10000:'))
litr = float(input('Ввести расход литра от 5 - 25:'))
gas = float(input('Стоимость бензина от 45 до 55:'))
if distance >= 100 and distance <= 10000:
    if litr >= 5 and litr <=25:
        if gas >= 45 and gas <= 55:
            print('Стоимость поездки:', distance / 100 * litr * gas)            
        else: 
            print('данные не корректные')
    else: 
        print('данные не корректные')
else: 
    print('данные не корректные')