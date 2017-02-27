import functools
import os

def log(prefix=None):
    def inner_log(f):
        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            result = f(*args)
            fname = f.__name__
            arglist = []
            if args:
                arglist.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in kwargs.items()]
                arglist.append(', '.join(pairs))
            if prefix:
                print('[{}] {}({})={}'.format(prefix, fname, arglist, result))
            else:
                print('{}({})={}'.format(fname, arglist, result))
            return result

        return wrapped_f
    return inner_log


@log(prefix=os.getpid())
def compute(x, y, op=int.__add__):
    return op(x, y)


if __name__ == '__main__':
    compute(3, 4)
    compute(3, 4, op=int.__mul__)

