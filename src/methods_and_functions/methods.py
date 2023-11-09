from sympy import *

def derivative(func, x0):
    x = Symbol('x')

    derivative = func.diff(x)
    f = lambdify(x, derivative)

    return f(x0)



def polovljenje_intervala(a, b):
    return (a + b) / 2

def regula_falsi_i_sjecica(a, func_a, b, func_b):
    if (func_b - func_a == 0):
        print ("Math error!")
        return

    fraction = (b - a) / (func_b - func_a)
    c = b - fraction * func_b

    return c

def newton_raphston(x0, func_x0, func):
    func_der = derivative(func, x0)

    fraction = func_x0 / func_der
    x = x0 - fraction

    return x

def newton_raphston_modified(x0, func_x0, func, first_x):
    func_der = derivative(func, first_x)

    fraction = func_x0 / func_der
    x = x0 - fraction

    return x
