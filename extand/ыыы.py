# int
# degree(int
# a, int
# b) // функция
# для
# возведения
# числа
# в
# степень
# {
#     int
# sum = 1;
# for (int
# i = 0;
# i < b;
# i + +)
# sum *= a;
# return sum;
# }
#
# int
# func_phi(int
# n) // функция
# Эйлера
# {
# int
# ret = 1;
# for (int i = 2; i * i <= n; ++i) {
# int p = 1;
# while (n % i == 0) {
# p *= i;
# n /= i;
# }
# if ((p /= i) >= 1) ret *= p * (i - 1);
# }
# return --n ? n * ret: ret;
# }
#
# bool
# PrimitiveRoot(int
# g, int
# m)
# {
# int
# phi = func_phi(m);
#
# char * arr = new
# char[phi];
# int
# size = 0;
# bool
# b = true;
#
# for (int i=0;(i <= phi-1 & & b);i++)
# {
#     int
# num = (degree(g, i) % m);
# for (int
# u = 0;
# u < size;
# u + +)
# {
# if (arr[u] == num)
# b = false;
# }
# arr[size] = num;
# size + +;
# }
# cout << "Is number " << g << " is a primitive root modulo " << m << ": " << b << endl;
# return b;
# }