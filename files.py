def read():
    numList = []
    with open("./dir/numbers.txt", "r", encoding = "utf-8") as f:
        for line in f:
            numList.append(int(line))
        print (numList)

def write():
    names = ["El Facun", "Miguelón", "Pepe", "Christian"]
    with open("./dir/names.txt", "a", encoding = "utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()


if __name__ == '__main__':
    run()