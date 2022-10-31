from sympy import *
import math

x = Symbol('x')

def func_1():
    f = math.e**x - 3*x -2
    return eval(str(f))

def func_2():
    f = sin(x) - x + 2
    return eval(str(f))

def func_3():
    f = x**2 - 2
    return eval(str(f))

def func_4():
    f = ln(x) + x - 3
    return eval(str(f))

def func_5():
    f = 2*sin(x) - sqrt(x-2)
    return eval(str(f))

def func_6():
    f = x**3 + 4*x**2 - 1
    return eval(str(f))

def func_7():
    f = x**3 - 2*x**2 - 1
    return eval(str(f))

def calc_func_1(param):
    f = lambdify(x, func_1())
    return f(param)
    # [-0.5; -0.2]

def calc_func_2(param):
    f = lambdify(x, func_2())
    return f(param)
    #[2.5; 2.7]

def calc_func_3(param):
    f = lambdify(x, func_3())
    return f(param)
    # [1, 2]

def calc_func_4(param):
    f = lambdify(x, func_4())
    return f(param)

def calc_func_5(param):
    f = lambdify(x, func_5())
    return f(param)

def calc_func_6(param):
    f = lambdify(x, func_6())
    return f(param)

def calc_func_7(param):
    f = lambdify(x, func_7())
    return f(param)