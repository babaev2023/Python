"""
Day_4\Homework6.py

Вывод символов E или N
Даны буквы(E или N) и масштаб (>= 7). Вывести букву с учетом масштабируемости(количество строк) символами *.
Формат входных данных: 
На вход программе буква E или N и цифра(количество строк)
Формат выходных данных
Требуется вывести буквы символами * (см. пример)

"""

letter = input("Enter E or N: ")
number = int(input("Enter a number, please: "))
if letter == "E":
    x = 0
    while x < number:
        if (x == 0 or x == number // 2 - 1 * (number % 2 == 0) or x == number - 1):
            print("*" * number)
        else:
            print("*" * 1)
        x += 1
elif letter == "N":
    i = 0
    while i < number:
        print("*" + ' ' * i + "*" + ' ' * (number - i - 1) + "*")
        i += 1
		
elif letter != "N" or letter != "E":
    i = 0
    while i < number:
        print("*")
        i += 1