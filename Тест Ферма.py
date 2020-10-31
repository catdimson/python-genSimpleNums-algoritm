# -- Программа реализации алгоритма теста Ферма --
import timeit
import random

karmikle = False
karmikle_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361]


def fast_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r





def test_Ferma(n):
    if n in karmikle_numbers:
        global karmikle
        karmikle = True
        return False
    a = random.randint(2, n-2)
    gcd, x0, y0 = algoritm_Euclid(n, a)
    if gcd != 1:
        return False
    # r = a ** (n-1) % n
    r = fast_pow(a, n-1, n)
    # a = 2
    print('a = {0}, r = {1}'.format(a, r))
    if r == 1:
        return True
    else:
        return False


n = int(input('Введите n: '))
print("Время: {0}".format(timeit.timeit("test_Ferma({0})".format(n), setup="from __main__ import test_Ferma", number=1)) + " sec.")
result = test_Ferma(n)
if result == True:
    print("Число {0} вероятно простое".format(n))
elif karmikle == True:
    print("Введенное вами число - число Кармайкла")
    print("Число {0} составное".format(n))
else:
    print("Число {0} составное".format(n))