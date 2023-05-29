f = open('test.txt', 'w')
print('Нажмите любую кнопку')
f.write('TEST')
content = input()
# если мы хотим принудительно записать файл - надо принудительно
# очистить буфер
f.flush()
f.close()


f = open('test.txt')
some = f.read(2) # 2 - это байт
print(some)
f.close()

f = open('test2.txt')
for line in f:
    print(line[:4])

content = f.read()
print('Пусто! len(content) = %s' % len(content))
f.close()
