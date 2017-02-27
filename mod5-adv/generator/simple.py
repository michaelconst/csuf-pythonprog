def odd_number_generator():
    n = 1
    while True:
        yield n
        n += 2


def odd_number_generator2():
    yield 1
    yield 3
    yield 5


def main():
    print('odd_number_generator type is {}'.format(type(odd_number_generator)))
    gen = odd_number_generator2()
    print('return value from odd_number_generator call is {}'.format(type(gen)))
    for i in gen:
        print(i)


if __name__ == '__main__':
    main()