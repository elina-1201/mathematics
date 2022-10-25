def get_function():
    print("\nOdaberite funkciju\n")

    print("[1] f(x) = e^x - 3x - 2")
    print("[2] f(x) = sin(x) - x + 2")
    print("[3] f(x) = x^2 - 2")

    function = input("\nUnesite ovdje: ")

    return function


def get_method():
    print("\nOdaberite metodu\n")

    print("[1] METODA POLOVLJENJA")
    print("[2] METODA REGULA FALSI")

    method = input("\nUnesite ovdje: ")

    return method


def get_absolute_error():
    print("\nUnesite eksponent dozvoljene apsolutne greske")
    absolute_error = input("\nUnesite ovdje: ")
    absolute_error = 10 ** float(absolute_error)

    return absolute_error

def get_interval():
    print("\nUnesite interval")
    a = input("\nUnesite donju granicu (a): ")
    b = input("\nUnesite gornju granicu (b): ")

    return float(a), float(b)

def get_float_format():
    print("\nUnesite koliko decimalnih mjesta ce se prikazivati u tabeli")
    float_frm = input("\nUnesite ovdje: ")

    return float_frm
