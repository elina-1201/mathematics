from pick import pick

def picker(options, title):
    selected = pick(options, title, indicator='=>')
    return selected[1]

def get_function():
    title = "\nOdaberite funkciju\n"

    func_1 = "f(x) = e^x - 3x - 2"
    func_2 = "f(x) = sin(x) - x + 2"
    func_3 = "f(x) = x^2 - 2"
    func_4 = "f(x) = ln(x) + x -3"
    func_5 = "f(x) = 2sin(x) - sqrt(x-2)"
    func_6 = "f(x) = x^3 + 4x^2 - 1"
    func_7 = "f(x) = x^3 - 2x^2 - 1"

    options = [func_1, func_2, func_3, func_4, func_5, func_6, func_7]

    return picker(options, title)

def get_method():
    title = "\nOdaberite metodu:\n"
    options = ['METODA POLOVLJENJA', 'METODA REGULA FALSI', 'NEWTON – RAPHSTONOVA METODA', "MODIFIKOVANA NEWTON – RAPHSTONOVA METODA", "METODA SJECICE"]

    return picker(options, title)


def get_absolute_error():
    print("\nUnesite eksponent dozvoljene apsolutne greske")
    absolute_error = input("\nUnesite ovdje: ")
    absolute_error = 10 ** float(absolute_error)

    return absolute_error

def get_interval(method):
    if(method == 2 or method == 3):
        x0 = input("\nUnesite pocetnu vrijednost (x0): ")
        return float(x0)

    else:
        print("\nUnesite interval")
        a = input("\nUnesite donju granicu (a): ")
        b = input("\nUnesite gornju granicu (b): ")

        return float(a), float(b)

def get_float_format():
    print("\nUnesite koliko decimalnih mjesta ce se prikazivati u tabeli")
    float_frm = input("\nUnesite ovdje: ")

    return float_frm
