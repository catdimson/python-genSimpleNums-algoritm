import timeit

def power(a, n, m):
    res = 1
    p = a % m
    while n:
        if (n & 1):
            res = (res * p) % m
        n >>= 1
        p = (p * p) % m
    return res

# a, n, m = map(int, input().split())
# print(power(a, n, m))


# Просто возведение в степень
def fast_pow(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = fast_pow(x, y / 2)
    p *= p
    if y % 2:
        p *= x
    return p


# Быстрое возведение в степень числа по модулю
def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r


n, a, m = int(input('n = ')), int(input('a = ')), int(input('m = '))
print("Время: {0}".format(timeit.timeit("pow_h({0}, {1}, {2})".format(a, n, m), setup="from __main__ import pow_h", number=1)) + " sec.")
print("result {0}".format(pow_h(124, 214, 24)))