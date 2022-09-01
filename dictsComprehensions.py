def run():

    keys = [i for i in range (1, 101)]
    vals = [i**3 for i in range (1, 101)]

    dic = {keys[k]: vals[k] for k in range (0, 100)}
    print (dic)

if __name__ == '__main__':
    run()


