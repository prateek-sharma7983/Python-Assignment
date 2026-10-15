products={
    "laptop":10,
    "mouse":3,
    "keyboard":0,
    "monitor":7,
    "printer":2
}

for product,stock in products.items():
    if stock==0:
        print("out of stock")
    elif stock<=5:
        print("low stock")
    else:
        print("available")