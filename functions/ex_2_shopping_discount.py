def calculate_discount(price,discount=None):
    if price<=0:
        print("invalid amount : ")
    elif price<1000:
        slab_discount=5
        
    elif price>=1000 and price<=4999:
        slab_discount=10
        
    elif price>=5000 and price<9999:
        slab_discount=15
        
    else:
        slab_discount=20
    if discount is not None:
        if discount<0 or discount>100:
            print("invalid discount")
            return
        final_discount=discount
    else:
        final_discount=slab_discount



    discount_amount=price*final_discount/100
    final_amount=price-discount_amount

    
            


    print("your original bill : ",price)
    print("your discount : ",final_discount, " %")
    print("your discounted amount : ",discount_amount)
    print("funal amount : ", final_amount)
calculate_discount(4000)

