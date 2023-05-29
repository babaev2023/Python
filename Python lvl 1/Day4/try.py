# Исключения

import os
import traceback  # если хотим сообщения об ошибках печатать,
# а программу не прерывать

try:
    f = open('b.txt')
except Exception as e:
    print('Произошла какая-то ошибка')
    print('Какая?', type(e), e)
    traceback.print_exc()
else:
    content = f.read()  # прочитать файл, если ошибка НЕ произошла
finally:
    print('Я закончил работу с файлом b.txt')

print('Я продолжаю работать несмотря ни на что')
