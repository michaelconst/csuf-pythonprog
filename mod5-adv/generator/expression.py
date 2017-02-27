def infinite_generator():
    n = 1
    while True:
        yield n
        n += 1


def main():
    for n in (x for x in infinite_generator() if x % 2 == 1):
        print(n)

if __name__ == '__main__':
    main()