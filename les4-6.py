# Итератор, генерирующий целые числа, начиная с указанного

from itertools import count

for num in count(3):
    if num > 10:
        break
    print(num)

# Итератор, повторяющий элементы некоторого списка, определённого заранее

from itertools import cycle

my_list = [1, 2, 3]

for i in cycle(my_list):
    if i > 10:
        break
    print(i)

    from itertools import cycle

    my_list = [1, 2, 3]
    counter = 0
    repeat_counter = 0

    for item in cycle(my_list):
        if repeat_counter == 10:
            repeat_counter = 0
            counter += 1
        if counter == len(my_list):
            break