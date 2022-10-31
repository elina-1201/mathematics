from assigns.ui_printing import *
from calculation.start_calculation_with_number import *
from calculation.start_calculation_with_interval import *
from clear_printing import execute_and_clear


def get_inputs():
    function = execute_and_clear(get_function)
    method = execute_and_clear(get_method)
    absolute_error = execute_and_clear(get_absolute_error)
    float_frm = execute_and_clear(get_float_format)

    if(method == 2 or method == 3):
        x0 = execute_and_clear(get_interval, method)
        start_calculation_with_number(function, method, absolute_error, x0,float_frm)
    else:
        a, b = execute_and_clear(get_interval, method)
        start_calculation_with_interval(function, method, absolute_error, a, b, float_frm)
