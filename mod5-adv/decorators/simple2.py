import functools


def log(f):
    @functools.wraps(f)
    def wrapped_f(*args, **kwargs):
        """
        Print the operation, its arguments and its result.
        :param args: operation's arguments
        :return: result of the operation
        """
        result = f(*args)
        fname = f.__name__
        arglist = []
        if args:
            arglist.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in kwargs.items()]
            arglist.append(', '.join(pairs))
        print('{}({})={}'.format(fname, arglist, result))
        return result

    print('inside the log decorator')
    return wrapped_f


@log
def compute(x, y, op=int.__add__):
    """
    Invoke the binary operation 'op' for arguments x and y.
    :param x: first operand
    :param y: second operand
    :param op: operation to execute
    :return: result of the operation
    """
    print('inside the compute function')
    return op(x, y)


if __name__ == '__main__':
    compute(3, 4)
    compute(3, 4, op=int.__mul__)

