def divisors(num):
    try:
        if ( num < 0 ):
            raise ValueError("Negative numbers are not allowed")
        divisors = []
        for i in range (1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
        
    except ValueError as ve:
        print(ve)
        return ''


def run():
    num = input('Type a number: ')
    assert num.isnumeric() and (int(num) >= 0), 'A non negative number must be introduced'
    print(divisors(int (num)))
    print ('End of the program')


if __name__ == '__main__':
    run()