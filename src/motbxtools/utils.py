from contextlib import contextmanager


@contextmanager
def open_conditional(*args, **kwds):
    """Open a file. Return None if type(file) is not a path-like object
    """
    if not args[0]:
        yield None
    else:
        open_file = open(*args, **kwds)
        try:
            yield open_file
        finally:
            open_file.close()
