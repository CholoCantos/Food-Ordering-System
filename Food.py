from Menu import menu
class food(menu):
    
    pansit = ""
    
    def __init__(self, name, price, quantity, pansit):
        self.menu_name = name
        self.price = price
        self.pansit = pansit
        self.quantity = quantity