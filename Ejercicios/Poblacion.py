
Import operator
d1 = {"Laredo": 100000, "Monterrey": 200000, "Saltillo": 250000}


def OrdenaCiudades(dic):
    do = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
    l = []
    for key, value in do.items():
        if value >= 200000:
            l += [key]
    print(l)


OrdenaCiudades(d1)
