'''Обчислити значення виразу
 f(2,a,4)-5*f(a,b,-c)
 де
 f(x,y,z) = lg(x+y-z),                     if x+y-z > 10,
            (fabs(x+y)+1)**z               if z-10<x+y<z+1,
            x**2 + y**2 - z**3             if x+y-z=1,
            cosx*cosx + siny -e**(2*z+1)    else
'''
# Допоміжний код
import math as m
def function(x,y,z):
    if x+y-z > 10:
        f = m.log10(x+y-z)
    elif z-10 < x+y < z+1:
        f = (m.fabs(x + y) + 1)**z
    elif x+y-z == 1 :
        f = x**2 + y**2 - z**3
    else: f = m.cos(x)*m.cos(x) + m.sin(y) - m.e**(2*z+1)
    return f
#-----------------------------------------------------------------------------------------------------------------------
# Позначення
"""
a,b,c - змінні float
v - результат обчислення
"""
# Введення
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
# Обчислення
v = function(2,a,4)-5*function(a,b,-c)


# Введення
print('Значення виразу = {0}'.format(v))