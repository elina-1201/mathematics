def polovljenje_intervala(a, b):
    return (a + b) / 2


def regula_falsi(a, func_a, b, func_b):
    if (func_b - func_a == 0):
        print ("Math error!")
        return

    razlomak = (b - a) / (func_b - func_a)
    c = b - razlomak * func_b

    return c
