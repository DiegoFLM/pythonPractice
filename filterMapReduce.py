from functools import reduce


def run():
    lst = [1, 4, 5, 6, 9, 13, 19, 21]
    print(lst)

    odd = list(filter(lambda x: (x % 2) != 0, lst))
    print (odd)

    powers = list( map(lambda x: x**2, lst) )
    print (powers)

    product = reduce(lambda x, y: x*y, lst)
    print(product)


if __name__ == '__main__':
    run()

