from assigns.assign_functions import *
from clear_printing import print_result
from methods_and_functions.methods import newton_raphston, newton_raphston_modified

def start_calculation_with_number(function, method, absolute_error, x0, float_frm):

    func_calc = assign_functions_calculation(function)
    func = assign_functions(function)

    match method:
        case 2:
            calculate_x = lambda: newton_raphston(x0, func_x0, func)
        case 3:
            calculate_x = lambda: newton_raphston_modified(x0, func_x0, func, first_x)

    first_x = x0
    E = 0
    x = 0
    i = 1

    table = [[0, x0, 0]]
    headers = ["№", "x", "E"]

    while True:
        func_x0 = func_calc(x0)

        E = x0
        x = calculate_x()
        E = abs(E - x)

        row = [i, x, E]

        table.append(row)

        x0 = x
        i += 1

        if (E <= absolute_error): break

    print_result(table, headers, float_frm)

    # │ 2.554196