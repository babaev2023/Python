
def ending(N, forms):
    '''Returns russian form of multiple count,
    using N as quantity and forms as array of
    [0]: 1 object, [1]: 2,3 or 4 objects, [2]: 5+ objects
    '''
    wordform = forms[2]
    if not(4 < N % 100 < 21):
        if N % 10 == 1:
            wordform = forms[0]
        elif 1 < N % 10 < 5:
            wordform = forms[1]  # 2, 3, 4
    return wordform

if __name__ == '__main__':
    print('Тесты и отладка')
else:
    print(__name__)
