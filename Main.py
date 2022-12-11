import os
#Importing the classes within the folder
from Menu import menu
from Food import food
from Drink import drink
from CreditCard import credit_card
from DebitCard import debit_card
from CashPayment import cash_payment

#If chosen is "O" it will display the function
def create_order():
    os.system('cls')
    order = []
    order_complete = False
    while(order_complete == False):
        print(" ~~~~~~~~~~~~~~~~~")
        print("\tMENU")
        print(" ~~~~~~~~~~~~~~~~~")
        print(" -----------------")
        print(" | 1. Main Items |")
        print(" | 2. Extras     |")
        print(" | 3. Drinks     |")
        print(" | 4. Pay Order  |")
        print(" -----------------")
        order_choice = input("\n Type Choice Here: ")

        if(order_choice == "1"):
            os.system('cls')
            print("\n\t   MAIN ITEMS")
            print("\n   Item\t\t\tPrice")
            print(" -------------------------------")
            print(" | 1: Pancit Guisado\t₱70.00 |")
            print(" | 2: Lomi Regular\t₱70.00 |")
            print(" | 3: Lomi Special\t₱75.00 |")
            print(" | 4: Lomi Jumbo\t₱90.00 |")
            print(" | 5: Chami\t\t₱70.00 |")
            print(" -------------------------------")
            food_choice = input("\n Type Choice Here: ")

            if(food_choice == "1"):
                toppings = input("\n\n Choose Toppings\n\n 1: Chicken Fillet\n 2: Pupor\n\n Type Choice Here: ")
                if(toppings == "1"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Pansit Guisado", 70.00, quantity, "Chicken Fillet"))
                    os.system('cls')
                elif(toppings == "2"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Pansit Guisado", 70.00, quantity, "Pupor"))
                    os.system('cls')

            elif(food_choice == "2"):
                toppings = input("\n\n Choose Toppings\n\n 1: Bola-Bola\n 2: Pupor\n\n Type Choice Here: ")
                if(toppings == "1"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Lomi Regular", 70.00, quantity, "Bola-Bola"))
                    os.system('cls')
                elif(toppings == "2"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Lomi Regular", 70.00, quantity, "Pupor"))
                    os.system('cls')
                else:
                    print("\n Invalid Input")
            elif(food_choice == "3"):
                toppings = input("\n\n Choose Toppings\n\n 1: Bola-Bola\n 2: Pupor\n\n Type Choice Here: ")
                if(toppings == "1"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Lomi Special", 75.00, quantity, "Bola-Bola"))
                    os.system('cls')
                elif(toppings == "2"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Lomi Special", 75.00, quantity, "Pupor"))
                    os.system('cls')
                else:
                    print("\n Invalid Input")
            elif(food_choice == "4"):
                toppings = input("\n\n Choose Toppings\n\n1: Bola-Bola\n2: Pupor\n\nType Choice Here: ")
                if(toppings == "1"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Lomi Jumbo", 90.00, quantity, "Bola-Bola"))
                    os.system('cls')
                elif(toppings == "2"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Lomi Jumbo", 90.00, quantity, "Pupor"))
                    os.system('cls')
                else:
                    print("\n Invalid Input")
            elif(food_choice == "5"):
                toppings = input("\n\n Choose Toppings\n\n 1: Chicken Fillet\n 2: Pupor\n\n Type Choice Here: ")
                if(toppings == "1"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Chami\t", 70.00, quantity, "Bola-Bola"))
                    os.system('cls')
                elif(toppings == "2"):
                    quantity = input("\n Enter quantity: ")
                    order.append(food(" Chami\t", 70.00, quantity, "Pupor"))
                    os.system('cls')
                else:
                    print("\n Invalid Input.")
            else:
                print(" \n Invalid input.")

        elif(order_choice == "2"):
            os.system('cls')
            print("\n\t    EXTRAS")
            print("\n Item\t\t\tPrice")
            print(" -------------------------------")
            print(" | 1. Chicharon\t\t₱25.00 |")
            print(" | 2. Plain Rice\t₱20.00 |")
            print(" | 3. Fried Rice\t₱30.00 |")
            print(" | 4. Extra Toppings\t₱50.00 |")
            print(" | 5. Atay\t\t₱35.00 |")
            print(" -------------------------------")
            side_choice = input("\n Type Choice Here: ")

            if(side_choice == "1"):
                quantity = input("\n Enter quantity: ")
                order.append(menu(" Chicharon", 25.00, quantity))
                os.system('cls')
            elif(side_choice == "2"):
                quantity = input("\n Enter quantity: ")
                order.append(menu(" Plain Rice", 10.00, quantity))
                os.system('cls')
            elif(side_choice == "3"):
                quantity = input("\n Enter quantity: ")
                order.append(menu(" Fried Rice", 20.00, quantity))
                os.system('cls')
            elif(side_choice == "4"):
                quantity = input("\n Enter Quantity: ")
                order.append(menu(" Extra Toppings", 50.00, quantity))
                os.system('cls')
            elif(side_choice == "5"):
                quantity = input("\n Enter Quantity: ")
                order.append(menu(" Atay      ", 35.00, quantity))
                os.system('cls')
            else:
                print("\n Invalid Input.")
            
        elif(order_choice == "3"):
            os.system('cls')
            print("\n\t    DRINKS")
            print("\n Item\t\t\tPrice")
            print(" -------------------------------")
            print(" | 1. Mineral Water\t₱15.00 |")
            print(" | 2. Coke Mismo\t₱20.00 |")
            print(" | 3. Mountain Dew\t₱20.00 |")
            print(" | 4. Pepsi\t\t₱20.00 |")
            print(" | 5. Royal\t\t₱20.00 |")
            print(" -------------------------------")
            drink_choice = input("\n Type Choice Here: ")
            
            if(drink_choice == "1"):
                quantity = input("\n Enter quantity: ")
                order.append(drink(" Mineral Water", 15.00, quantity))
                os.system('cls')
            elif(drink_choice == "2"):
                quantity = input("\n Enter quantity: ")
                order.append(drink(" Coke Mismo", 20.00, quantity))
                os.system('cls')
            elif(drink_choice == "3"):
                quantity = input("\n Enter quantity: ")
                order.append(drink(" Mountain Dew", 20.00, quantity))
                os.system('cls')
            elif(drink_choice == "4"):
                quantity = input("\n Enter quantity: ")
                order.append(drink(" Pepsi\t", 20.00, quantity))
                os.system('cls')  
            elif(drink_choice == "5"):
                quantity = input("\n Enter quantity: ")
                order.append(drink(" Royal\t", 20.00, quantity))
                os.system('cls')
            else:
                print("\n Invalid Input.")  
                
        elif(order_choice == "4"):
            order_complete = True
        
        else:
            print("\n Invalid input.")

    return order

#Displays the receipt after paying for the order
def print_history():
    os.system('cls')
    print("\n\n")
    print(" Credit Card Receipts: ")
    for i in range(0,len(credit_history)):
        credit_history[i].print_receipt()
    print(" Debit Card Receipts: ")
    for i in range(0,len(debit_history)):
        debit_history[i].print_receipt()
    print(" Cash Receipts: ")
    for i in range(0,len(cash_history)):
        cash_history[i].print_receipt()

#Displays the available Method of Payments
def print_mop():
    print(" ------------------")
    print(" | 1: Credit Card |")
    print(" | 2: Debit Card  |")
    print(" | 3: Cash        |")
    print(" | 4: Cancel      |")
    print(" ------------------")
#Payment Function
def start_pay(order):
    os.system('cls')
    print("\n\t\t\tPAYMENT")
    subtotal = 0.0
    for i in range(0,len(order)):
        subtotal = (subtotal + (float(order[i].price) * float(order[i].quantity)))
    total = ((subtotal * 0.07) + subtotal)
    print("\n Item\t\t\tPrice\t\t\tQuantity")
    for x in range(0,len(order)):
        
            print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print( order[x].menu_name + "\t\t₱" + str(order[x].price) + "\t\t\t   " + str(order[x].quantity))
            print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\n Subtotal: ₱%.2f\n" %(subtotal))
    print(" Total: ₱%.2f" %(total))
    print("\n\n Choose payment method\n")
    print_mop()

    choice = input(" Enter mode of payment: ")
