"""From https://medium.com/better-programming/advanced-python-consider-these-10-elements-when-you-define-python-functions-61c0be8a10ed.


Examples
--------
    @logging_time
    def calculate_integer_sum(n):
        return sum(range(n))

    @logging_time
    def calculate_integer_square_sum(n):
        return sum(x*x for x in range(n))

    calculate_integer_sum(10000)
    calculate_integer_sum time elapsed: 0.00027
    calculate_integer_square_sum(10000)
    calculate_integer_square_sum time elapsed: 0.00110

"""

from time import time

# Create the decorator function
def logging_time(func):
    def logged(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f"{func.__name__} time elapsed: {elapsed_time:.5f}")

    return logged
