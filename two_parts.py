"""
}<ДАНИЕ
--------------------------------------------------------------------------------
На вход получаем строку, нужно разрезать ее на 2 равные части и вернуть их
по отдельности. Если длина строки - нечетное число,
то первая часть должна быть меньше на 1 символ

Задачу можно решить 2 способами:
    - используя math
    - используя операторы

ПРИМЕРЫ
--------------------------------------------------------------------------------
- 'hello world' -> ('Hello ', 'world')
- 'hello' -> ('hel', 'lo')
- 'some' -> ('so', 'me')
"""
import math

def split_to_parts(str_to_split: str) -> tuple:
    """Разделяет строку на 2 части. Если длина строки нечетная, то первая часть
    на один символ больше

    :param str_to_split: строка для разделения
    :type str_to_split: str

    :return: кортеж с двумя частями
    :rtype: tuple
    """
    """ решение я подсмотрела и гугле. мне здесь непонятна необходимость и расположение ':'. и не понятно, куда divmod засунуть"""

    part_1 = str_to_split[int(len(str_to_split)/2):]
    part_2 = str_to_split[:int(len(str_to_split)/2)]
    return part_1, part_2


if __name__ == '__main__':
    string = input('Введите строку для разбивки: ')
    print(f"Результат: {split_to_parts(string)}")
