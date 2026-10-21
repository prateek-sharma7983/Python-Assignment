def calculate_discount(price,discount=5):
    if price<=0:
        print("invalid amount : ")
    elif price<1000:
        discount=5
        dis_amount=price*discount/100
        final_amount=price-dis_amount
    elif price>=1000 and price<=4999:
        discount=10
        dis_amount=price*discount/100
        final_amount=price-dis_amount
    elif price>=5000 and price<9999:
        discount=15
        dis_amount=price*discount/100
        final_amount=price-dis_amount
    elif price>=1000:
            discount=20
            dis_amount=price*discount/100
            final_amount=price-dis_amount


print("your original bill : ",price)
print("your discount : ",discount)
print("your discounted amount : ",discounted_amount)
print("funal amount : ", final_amount)
calculate_discount(4000)

