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
    try:
        num = int (input('Type a number: '))
        print(divisors(num))
        print ('End of the program')
    except ValueError:
        print('Only numbers are allowed')

if __name__ == '__main__':
    run()