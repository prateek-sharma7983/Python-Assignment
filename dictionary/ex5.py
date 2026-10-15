data={
    "a":10,
    "b":15,
    "c":20,
    "d":35,
    "e":40
}

for key,value in data.items():
    if value%2==0:
        if value>=20:
            print("large even")
        else:
            print("even")
    else:
        print("odd")