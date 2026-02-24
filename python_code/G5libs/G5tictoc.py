import time

__all__ = ['Timer']


class Timer(object):
    '''Timer helper — works like MATLAB tic/toc.

    Example with statement:
        with Timer() as timer:
            # your code here
        print(timer.elapsed)

    Example tic/toc:
        timer = Timer()
        timer.tic()
        # your code here
        print(timer.toc())
    '''

    def __init__(self, do_print=False):
        self._do_print = do_print
        self._start_time = 0
        self.elapsed = 0

    def __enter__(self):
        self.tic()
        return self

    def __exit__(self, type, value, traceback):
        self.toc()
        if self._do_print:
            print('Elapsed time is %f seconds.' % self.elapsed)

    def tic(self):
        self._start_time = time.time()

    def toc(self):
        self.elapsed = time.time() - self._start_time
        return self.elapsed
