def items(*prices):
    print("Prices : ",prices)
    print("Total : ",sum(prices))
prices=[100,200,300,400,500]
items(*prices)

def customer_details(name,city,member):
    print("name : ",name)
    print("city : ",city)
    print("membership : ",member)
details={"name" : "Prateek","city":"Bareilly","member":"gold"}
customer_details(**details)