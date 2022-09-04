def palindrome(string):
    assert len(string) > 0, 'Empty strings are not allowed'
    return string == string[::-1]


def run():
    try:
        print ( palindrome('') )    
    except TypeError:
        print('Only strings are allowed')


if __name__ == '__main__':
    run()