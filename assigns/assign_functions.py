from functions import *

def assign_functions(function):
    match function:
        case "1":
            return calc_func_1
        case "2":
            return calc_func_2
        case "3":
            return calc_func_3
