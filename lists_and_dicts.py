def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Diego", "lastname": "Ledesma"}

    super_list = [
        {"firstname": "Diego", "lastname": "Ledesma"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "García"}
    ]

    super_dict = {
        "some_naturals": [1, 2, 3, 4, 5],
        "some_integers": [-2, -1, 0, 1, 2],
        "some_floats": [1.1, 4.5, 6.43]
    }

    for dic in super_list:
        #print([(k, dic[k]) for k in dic])
        #print ( dic )
        for key, val in dic.items():
            print (key, "\t- ", val)

    for key, value in super_dict.items():
        print(key, "\t-", value)

if __name__ == '__main__':
    run()