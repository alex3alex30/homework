'''
Напишите функцию, которая читает и распечатывает текстовый файл.
Напишите декоратор к этой функции,
который печатает название файла и количество слов в нем
'''


def decorator(func):
    def wrapper(filename):
        print(filename)
        with open(filename, 'r') as file:
            counter = 0
            for line in file:
                words = line.rstrip('\n').split(' ')
                for word in words:
                    if word.isalnum():
                        counter += 1
        return counter
    return wrapper

@decorator
def readtext(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line, end = '')
