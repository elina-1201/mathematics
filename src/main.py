from assigns.get_inputs import *
from start_calculation import *
from clear_printing import execute_and_clear

def start_app():
    function = execute_and_clear(get_function)
    method = execute_and_clear(get_method)
    absolute_error = execute_and_clear(get_absolute_error)
    a, b = execute_and_clear(get_interval)
    float_frm = execute_and_clear(get_float_format)

    start_calculation(function, method, absolute_error, a, b, float_frm)

start_app()