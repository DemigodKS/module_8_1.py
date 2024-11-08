
def add_everything_up(a, b):

    try:
            d = a + b
            print(d)
    except TypeError as exc:
            c = str(a) + str(b)
            print(c)


print('Пример № 1')
print('-----------')
add_everything_up(5, 5.543)
print('')
print('Пример № 2')
print('-----------')
add_everything_up('ads', 5)
add_everything_up(17, 'hello')
print()
print('Пример № 3')
print('-----------')
add_everything_up('ads', 5.543)
add_everything_up(3.17, '45')




