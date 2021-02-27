#!usr/bin/python
# -*- coding: utf-8 -*-
import time


def measure(func, *args, time_measurement_function=time.perf_counter_ns, **kwargs):
    """ Executes the given function with params, measures and prints execution time

    Args:
        func - function that shall be executed
        args - tuple of params for func
        time_measurement_function - function that shall be used for time measurement

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
        print(f'Execution have taken {delta / 10E+06} ms')
    return result


def get_execution_time(func, *args, time_measurement_function=time.perf_counter_ns, **kwargs):
    """ Executes the given function with params, measures and returns the execution time

    Args:
        func - function that shall be executed
        args - tuple of params for func
        time_measurement_function - function that shall be used for time measurement

    Returns:
        result, time required for the execution of function

    """
    start_time = time_measurement_function()
    result = func(*args, **kwargs)
    end_time = time_measurement_function()
    return result, end_time - start_time
