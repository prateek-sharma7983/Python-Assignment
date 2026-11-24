class Bank:
    bank_name="BOI"
    rate_of_interest=12.50
    @staticmethod
    def simple_interest(prin,n):
        si=(prin*n*Bank.rate_of_interest)/100
        return si
b1=Bank()
b1.simple_interest(2000,5)
# print(Bank.simple_interest(2000,5))
        