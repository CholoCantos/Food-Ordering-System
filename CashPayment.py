import os
from ModeOfPayment import mode_of_payment
class cash_payment (mode_of_payment):
  amount_given = 0.0
  change = 0.0

  def set_amount_given (self, a):
      self.amount_given = a

  def calc_change (self):
      self.change = self.amount_given - self.amount

  def __init__(self, cust_name, amount, given):
        self.set_customer_name(cust_name)
        self.set_amount_due(float(amount))
        self.set_amount_given(int(given))
        self.calc_change()

  def print_receipt(self):
    print("\n\n\t   Cash Receipt\n")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Name: " + self.customer_name)
    print(" Total: ₱%.2f" %(self.amount))
    print(" Time: " + self.timeStamp)
    print(" Change: ₱%.2f" %(self.change))
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n")
