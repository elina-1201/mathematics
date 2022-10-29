def assign_vars(func_a, func_b, func_c, a, b, c):
    is_the_solution = False

    if(func_a * func_c < 0):
        a = a
        b = c
    elif(func_b * func_c < 0):
        b = b
        a = c
    elif(func_a * func_c == 0):
        is_the_solution = True

    return a, b, is_the_solution