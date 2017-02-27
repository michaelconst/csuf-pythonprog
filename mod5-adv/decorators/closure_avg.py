
def averager():
    data = list()

    def get_avg(val):
        data.append(val)
        res = sum(data) / len(data)
        return res

    return get_avg


def averager2():
    sum = 0
    length = 0

    def get_avg(val):
        nonlocal sum, length
        sum += val
        length += 1
        return sum / length
        return res

    return get_avg


if __name__ == '__main__':
    avg = averager2()
    print('average=%.2f' % avg(20))
    print('closure: {}, {}'.format(avg.__closure__[0].cell_contents, avg.__closure__[1].cell_contents))
    print('average=%.2f' % avg(23))
    print('closure: {}, {}'.format(avg.__closure__[0].cell_contents, avg.__closure__[1].cell_contents))
    print('average=%.2f' % avg(27))
    print('closure: {}, {}'.format(avg.__closure__[0].cell_contents, avg.__closure__[1].cell_contents))

    print('local vars: {}'.format(avg.__code__.co_varnames))
    print('free vars: {}'.format(avg.__code__.co_freevars))

