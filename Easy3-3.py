# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_len(*args):
    len_max = ''
    for ar in args:
        if len(ar) > len(len_max):
            len_max = ar
    print(len_max)


max_len('asd', 'as', 'arequ', 'a')
