products={
    "mobile":150000,
    "mouse":500,
    "laptop":60000,
    "keyboard":1200
}

for product,price in products.items():
    if price>=1000:
        if price>=5000:
            print(product, " is a Premium Product")
        else:
            print(product, " is an expensive product")
    else:
        print(product, " is a affordable product")