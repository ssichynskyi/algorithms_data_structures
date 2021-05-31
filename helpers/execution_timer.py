#!usr/bin/python
# -*- coding: utf-8 -*-
import time


def measure(func, *args, time_measurement_function=time.perf_counter_ns, **kwargs):
    """ Executes the given function with params, measures and prints execution time

    Args:
        func: function that shall be executed
        args: tuple of params for func
        time_measurement_function: function that shall be used for time measurement
        shall return time in ns

    Returns:
        result of execution of func with args, prints execution timestamps and time in console

    """
    start_time = time_measurement_function()
    print(f'Start at: {start_time} ns')
    result = func(*args, **kwargs)
    end_time = time_measurement_function()
    print(f'Finish at: {end_time} ns')
    delta = end_time - start_time
    if delta <= 0:
        print('Execution time not measurable, solution is too fast')
    else:
        print(f'Execution have taken {delta / 1E+06} ms')
    return result


def get_execution_time(func, *args, time_measurement_function=time.perf_counter_ns, **kwargs):
    """ Executes the given function with params, measures and returns the execution time

    Args:
        func: function that shall be executed
        args: tuple of params for func
        time_measurement_function: function that shall be used for time measurement

    Returns:
        result, time required for the execution of function

    """
    start_time = time_measurement_function()
    result = func(*args, **kwargs)
    end_time = time_measurement_function()
    return result, end_time - start_time


def compare_functions(data, check_function, *functions):
    """Runs all functions given in *functions on the same data

    It is important that all functions have the same signature.
    Verification of the result is done using check_function and
    returns of the functions if they return value or their data copy if not.
    If check function is None, Verification value is set "not verified"

    Args:
        data: data on which functions shall be run
        check_function: function which is used to prove the correctness of tested functions.
        Must return boolean value, where True is check is successful and False is fail.
        *functions: functions which need to be run to get the time

    Returns:
        a dict containing the verification result by check function and
        time, required for the execution of every function on given data
        Example:
            {'get_max': {'Verification': True, 'time ms': 1248732}}

    """
    if check_function is None:
        def check_function(*any_args): return 'Not verified'
    results = dict()
    for function in functions:
        local_data = data.copy()
        return_value, exec_time = get_execution_time(function, local_data)
        results[function.__name__] = {
            'Verification': check_function(local_data) if return_value is None else check_function(return_value),
            'time ms': exec_time / 1e+6
        }
    return results
