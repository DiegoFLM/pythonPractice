def run():
    #Intermediate Python class 8.
    #powers = []
    #for n in range(1, 101):
    #    if ( n % 3 == 0 ): continue
    #    powers.append( pow( n, 2) )
    #print ( powers )

    squares = [i**2 for i in range (1, 101) if i % 3 != 0]
    print (squares)

if __name__ == '__main__':
    run()


