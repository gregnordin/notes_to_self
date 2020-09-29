# timer.py
# Modified version of Python Timer Functions: Three Ways to Monitor Your Code

import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    """Time how long python code takes to execute and print to standard out.

    Usage
    -----
    timer = Timer()
    timer.start()
    <<multiple lines of python code>>
    timer.stop("Some message text 1")  # Or timer.stop() if you don't have custom text.

    # Later in code, the timer can be re-used.
    timer.start()
    <<multiple lines of python code>>
    timer.stop("Some message text 2")  # Or timer.stop() if you don't have custom text.

    Output
    ------
    Some message text 1: X.XXXX seconds
    Some message text 2: Y.YYYY seconds
    """

    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self, msg=""):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        if msg:
            print(f"{msg}: {elapsed_time:0.4f} seconds")
        else:
            print(f"Elapsed time: {elapsed_time:0.4f} seconds")
