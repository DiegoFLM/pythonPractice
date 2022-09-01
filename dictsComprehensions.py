import math

def run():

    dict = {i : round(math.sqrt(i), 2) for i in range(1, 1001)}
    print (dict)
if __name__ == '__main__':
    run()


