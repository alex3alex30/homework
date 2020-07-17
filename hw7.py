'''
1. Напишите функцию, которая возвращает список файлов из директории.

2. Напишите декоратор для этой функции, который распечатает все файлы с

раcширением .log из найденных
'''

import os
import io
def find_log(func):
    def wrapper():
        for name in func():
            if name.endswith('.log'):
                print(name)
                with open(name) as fo: # analog fo.readlines() полностью читаем файл и забиваем память
                    for line in fo:
                        print(line, end='')
                    # print(fo.read())  # прочитать весь файл как одну строчку
        return func()
    return wrapper


@find_log
def list_files():
    path = '/Users/alexcherniyenko/Desktop/homework'
    files_list = os.listdir(path)
    return files_list
