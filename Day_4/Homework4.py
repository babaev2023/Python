﻿"""
Day_4\Homework4.py

С клавиатуры вводится 10 целых чисел. 
Вывести количество введенных нечетных положительных. 
Функцию input() используем в коде один раз. 
Формат входных данных
Вводится 10 целых чисел.
Формат выходных данных
Выведите ответ на задачу.
"""

a = 1
counter = 0  # счетчик нечетных чисел

while a <= 10:
    number = int(input("Введите число: "))
    if number > 0 and number % 2 != 0:
        counter += 1   
    a += 1    
        
print(counter)