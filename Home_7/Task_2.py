'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
'''
import os

os.system('cls')


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        rows = []
        for j in range(1, num_columns + 1):
            rows.append(str(operation(i, j)))
            print(operation(i, j), end='\t')
        print()

print_operation_table(lambda x, y: x * y)
