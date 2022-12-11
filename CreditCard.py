import random
from CardPayment import card_payment
class credit_card(card_payment):
  zip_code = "0"

  def set_zip(self, z):
      self.zip_code = z

  def __init__(self, cust_name, amount, zip_code):
      self.set_customer_name(cust_name)
      self.set_amount_due(float(amount))
      self.set_card_no(random.randint(1000,9999))
      self.set_zip(zip_code)
      self.confirmation_no = random.randint(100,999) 