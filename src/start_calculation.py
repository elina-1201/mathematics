from assigns.assign_functions import *
from methods import *
from assigns.assign_vars import *
from clear_printing import print_result

def start_calculation(function, method, absolute_error, a, b, float_frm):
    match method:
        case "1":
            calculate_c = lambda: polovljenje_intervala(a, b)
        case "2":
            calculate_c = lambda: regula_falsi(a, func_a, b, func_b)

    func = assign_functions(function)

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

        a, b, is_the_solution = assign_vars(func_a, func_b, func_c, a, b, c)
        i += 1

        if(is_the_solution): break
        if (E <= absolute_error): break

    print_result(table, headers, float_frm)

    # print(f'{i} | {a:.6f} | {func_a:.6f} | {b:.6f} | {func_b:.6f} | {c:.6f} | {E:.6f}')