from tabulate import tabulate
import os

def print_result(table, headers, float_frm):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(tabulate(table, headers, floatfmt=f".{float_frm}f", tablefmt="rounded_grid",  numalign="center"))

    os.system('PAUSE' if os.name == 'nt' else 'read -p ""')

def execute_and_clear(function, *args):
    os.system('cls' if os.name == 'nt' else 'clear')
    return function(*args)