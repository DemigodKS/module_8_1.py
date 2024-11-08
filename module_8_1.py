
def add_everything_up(a, b):

    try:
            c = str(a) + str(b)
            print(c)
            d = a + b
            print(d)
    except TypeError as exc:
        print('Нельзя складывать значения', type(a), 'и', type(b), f'ERROR!:{exc}')

print('Пример № 1')
print('-----------')
add_everything_up(5, 5.543)
print('')
print('Пример № 2')
print('-----------')
add_everything_up('ads', 5)
print()
add_everything_up(17, 'hello')
print()
print('Пример № 3')
print('-----------')
add_everything_up('ads', 5.543)
print()
add_everything_up(3.17, '45')




