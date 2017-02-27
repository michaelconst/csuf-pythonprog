
def log(f):
    def wrapped_f(*args):
        print('args={}'.format(args))
        result = f(*args)
        print('result=%d' % result)
        return result

    print('inside the log decorator')
    return wrapped_f


@log
def add(x, y):
    print('inside the add function')
    return x + y

# def add(x, y):
#     print('inside the add function')
#     return x + y


if __name__ == '__main__':
    add(3, 4)
#     new_add = log(add)
#     new_add(3, 4)
