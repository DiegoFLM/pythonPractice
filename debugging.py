def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors




def run():
    num = int (input('Type a number: '))
    print(divisors(num))
    print ('End of the program')


if __name__ == '__main__':
    run()