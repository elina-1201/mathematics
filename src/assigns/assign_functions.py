from methods_and_functions.functions import *

def assign_functions_calculation(function):
    match function:
        case 0:
            return calc_func_1
        case 1:
            return calc_func_2
        case 2:
            return calc_func_3
        case 3:
            return calc_func_4
        case 4:
            return calc_func_5
        case 5:
            return calc_func_6
        case 6:
            return calc_func_7

def assign_functions(function):
    match function:
        case 0:
            return func_1()
        case 1:
            return func_2()
        case 2:
            return func_3()
        case 3:
            return func_4()
        case 4:
            return func_5()
        case 5:
            return func_6()
        case 6:
            return func_7()
