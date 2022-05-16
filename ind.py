#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import math

"""
С использованием многопоточности для заданного значения найти сумму ряда с точностью члена ряда по абсолютному
значению 1e-07 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных
рядов.
"""

CONST_ABSOLUTE = 1e-07


# Находим контрольное значение
def control_x(x=0.7):
    return 1 / (1 - x)


def control_y(x=-0.8):
    return 5 - 2 * x / (6 - 5 * x + math.pow(x, 2))


def summ_1(x):
    s = 0
    n = 0
    curr = 0
    while True:
        pre = math.pow(x, n)
        n += 1
        if abs(curr - pre) < CONST_ABSOLUTE:
            break
        curr = math.pow(x, n)
        s += curr
    return s


def summ_2(x):
    s = 0
    n = 0
    curr = 0
    while True:
        previous = (1 / math.pow(2, n) + 1 / math.pow(3, n)) * math.pow(x, n-1)
        n += 1
        if abs(curr - previous) < CONST_ABSOLUTE:
            break
        curr = (1 / math.pow(2, n) + 1 / math.pow(3, n)) * math.pow(x, n-1)
        s += curr
    return s


def compare(first, second, x):
    result = first(x) - second(x)
    print(f"Результат сравнения {result}")


if __name__ == '__main__':
    th1 = Process(target=compare(summ_1, control_x, 0.7))
    th2 = Process(target=compare(summ_2, control_y, -0.8))
    th1.start()
    th2.start()
    th1.join()
    th2.join()