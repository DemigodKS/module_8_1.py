

def add_everything_up(a, b):

    try:
            d = a + b
            return d
    except TypeError as exc:
            c = str(a) + str(b)
            return c


print('Пример № 1')
print('-----------')
print(add_everything_up(5, 5.54))
print('')
print('Пример № 2')
print('-----------')
print(add_everything_up('ads', 5))
print(add_everything_up(17, 'hello'))
print()
print('Пример № 3')
print('-----------')
print(add_everything_up('ads', 5.54))
print(add_everything_up(3.17, '45'))










