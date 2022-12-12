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
    
    #Credit Card Receipt
    if (choice == "1"):
        print("\n")
        temp_name = input(" Enter a name for the order: ")
        temp_amount = total
        temp_zip = input(" Enter Zip code: ")
        temp_payment = credit_card(temp_name, temp_amount,temp_zip)
        credit_history.append(temp_payment)
        credit_history[len(credit_history)-1].print_receipt()
        

    # Debit Card Receipt
    elif(choice == "2"):
        print("\n")
        temp_name = input(" Enter a name for the order: ")
        temp_amount = total
        temp_pin = input(" Enter pin: ")
        debit_history.append(debit_card(temp_name, temp_amount, temp_pin))
        debit_history[len(debit_history)-1].print_receipt()
        

    #Cash Payment Receipt
    elif(choice == "3"):
        print("\n")
        temp_name = input(" Enter a name for the order: ")
        temp_given = input(" Enter amount received: ₱")
        if (float(temp_given) >= total):
            cash_history.append(cash_payment(temp_name, total, temp_given))
            cash_history[len(cash_history)-1].print_receipt()
        else:
            print(" Insufficient amount given.")


    elif(choice == "4"):
        os.system('cls')
        return
    
    else:
        print(" Invalid input")

credit_history = []
debit_history = []
cash_history = []

#Main Function -- Opening Screen
def main(): 
    user_input = "0"
    while(user_input != "E"):
        print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ~~~~~~~~~~~~~~~~~   PANSITERIA  ~~~~~~~~~~~~~~~~~~~~")
        print(" ~~~~~~~~~~~~~~~~~   MAGNIFICO   ~~~~~~~~~~~~~~~~~~~~")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n   [O]: Start new order\t[R]: Receipts\t [E]: Exit")
        user_input = input("\n   Enter your choice here: ").upper()
        if(user_input == "O"):
            start_pay(create_order())
        elif(user_input == "R"):
            print_history()
        elif(user_input == "E"):
            exit()
        else:
            print(" Invalid Input. Try Again")
#Calling the main function
main()

