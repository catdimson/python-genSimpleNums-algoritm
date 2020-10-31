# -- Программа реализации алгоритма теории делимости --
import math
import timeit


def test_of_divisibility(num):
    for i in range(math.trunc(math.sqrt(num)), 1, -1):
        print(i)
        if num % i == 0:
            return True
    return False


data = int(input('Введите число: '))
result = test_of_divisibility(data)
print("Время: {0}".format(timeit.timeit("test_of_divisibility({0})".format(data), setup="from __main__ import test_of_divisibility", number=1)) + " sec.")
print("Составное: {0}".format(result))