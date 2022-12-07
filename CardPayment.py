import random
from ModeOfPayment import mode_of_payment
class card_payment(mode_of_payment):
    card_no = 0
    confirmation_no = 0

    def set_card_no (self, c):
        self.card_no = c


    def __init__(self, cust_name, amount):
        self.set_customer_name(cust_name)
        self.set_amount_due(float(amount))
        self.set_card_no(random.randint(1000,9999))
        self.confirmation_no = random.randint(100,999)

    def print_receipt(self):
        print("\n\n\t   Card Receipt\n")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" Name: " + self.customer_name)
        print(" Card No: XXXXXXXX" + str(self.card_no))
        print(" Confirmation Number: " + str(self.confirmation_no))
        print(" Total: ₱%.2f" %self.amount)
        print(" Time : " + str(self.timeStamp))
        print(" Signature: ___________")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")


