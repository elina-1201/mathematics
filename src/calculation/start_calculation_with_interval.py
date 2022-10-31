from assigns.assign_functions import *
from assigns.assign_vars import *
from clear_printing import print_result
from methods_and_functions.methods import polovljenje_intervala, regula_falsi_i_sjecica


def start_calculation_with_interval(function, method, absolute_error, a, b, float_frm):
    match method:
        case 0:
            calculate_c = lambda: polovljenje_intervala(a, b)
        case 1 | 4:
            calculate_c = lambda: regula_falsi_i_sjecica(a, func_a, b, func_b)

    func = assign_functions_calculation(function)

    E = 0
    c = 0
    i = 1

    table = []
    headers = ["№", "a", "f(a)", "b", "f(b)", "c", "E"]

    while True:
        E = c

        func_a = func(a)
        func_b = func(b)

        c = calculate_c()
        func_c = func(c)

        E = abs(E - c)

        row = [i, a, func_a, b, func_b, c]

        if(i==1):
            row.append(0)
        else:
            row.append(E)

        table.append(row)

        if(method == 4):
            a = b
            b = c
        else:
            a, b, is_the_solution = assign_vars(func_a, func_b, func_c, a, b, c)
            if(is_the_solution): break

        i += 1        
        if (E <= absolute_error): break

    print_result(table, headers, float_frm)