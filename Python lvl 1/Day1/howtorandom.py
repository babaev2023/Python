# Домашнее задание: БЫКИ И КОРОВЫ
# Компьютер "загадывает" число из 4 разных цифр
# человек пытается его угадать
# Простое задание: компьютер отвечает, больше
#    загадываемое число предполагаемого или меньше
# Сложное задание: компьютер отвечает, сколько цифр
#   присутствуют, но стоят на ЧУЖИХ местах (коровы)
#   присутствуют и стоят на СВОИХ местах - (быки)
##БЫКИ (на своих местах) И КОРОВЫ (просто встречаются)


import random

# Генерируем цифры 
numberxxxx = ''
xxxx = 4 
for i in range (xxxx):
    numberxxxx += str(random.randint(0,9))
#print ("Правильный ответ: ", numberxxxx)

score = 0

answer = input ("Введите число из 4 цифр без пробелов :")
while (len(answer) != len(numberxxxx)) or (answer.isdigit() != True):
    answer = input ("Введите корректно! - 4 цифры без пробелов :")

while answer != numberxxxx:
	cow = 0
	bulls = 0
	for i in range (0,xxxx):
	    if answer[i] in numberxxxx:
		    cow += 1
	for i in range (0,xxxx):
	    if answer[i] == numberxxxx [i]:
		    bulls +=1
	print("Быки: ", bulls)
	print("Коровы: ", cow -bulls)
	score +=1
	answer = input("Еще одна попытка! ")
	while (len(answer) !=len(numberxxxx)) or (answer.isdigit() !=True):
	    answer = input ("Введите корректно! - 4 цифры без пробелов :")

print ("Поздравляем! Вы угадали за", score, "ходов!")		

