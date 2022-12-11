import time
class mode_of_payment:
    customer_name = ""
    amount = 0.0

    timeStamp = time.asctime()

    def set_customer_name (self, c):
        self.customer_name = c
    def set_amount_due (self, a):
        self.amount = a

    def __init__(self, cust_name, amount):
        self.set_customer_name(cust_name)
        self.set_amount_due(int(amount)*0.07 + int(amount))