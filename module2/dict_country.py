def run():
    my_dictionario = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }
    print(my_dictionario['key1'])
    print(my_dictionario['key2'])
    print(my_dictionario['key3'])

    population_countries = {
        'Argentina': 2,
        'Brazil': 5,
        'Colombia': 2,
    }
    m=0
    for countrie in population_countries.keys():
        print(countrie)

    for countrie in population_countries.values():
        m+= countrie
        print(m)

    for countrie, poblacion in population_countries.items():
        print(countrie + ' tiene ' + str(poblacion) + ' habitantes ')

if __name__ == "__main__":
    run()