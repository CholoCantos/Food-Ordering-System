import random
from CardPayment import card_payment
class debit_card(card_payment):
  pin = 0

  def set_pin(self, p):
      self.pin = p

  def __init__(self, cust_name, amount, pin):
      self.set_customer_name(cust_name)
      self.set_amount_due(float(amount))
      self.set_card_no(random.randint(1000,9999))
      self.set_pin(pin)
      self.confirmationNo = random.randint(100,999)