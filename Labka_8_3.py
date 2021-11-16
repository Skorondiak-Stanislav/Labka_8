"""
Нехай x_0=2,x_1=1, x_i=cos(x_i_1)**(x_i_2) . Визначити x_n  .

"""
# Позначення
"""
n - номер числа
s - значення числа
"""
from math import *
# Введення
n = int(input("n="))
# Допоміжний код
def function(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 9
    else:
        return cos(function(n-1))**(function(n-2))
# Обчислення
s = function(n)
# Виведення
print("x_{0} = {1:.2f}".format(n,s))
