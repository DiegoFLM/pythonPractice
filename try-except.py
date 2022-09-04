def palindrome(string):
    try:
        if (len(string) == 0):
            raise ValueError("Empty strings are not allowed")
        return string == string[::-1]

    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        print ( palindrome( 7 ) )    
    except TypeError:
        print('Only strings are allowed')


if __name__ == '__main__':
    run()