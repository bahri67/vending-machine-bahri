
menu = {
    "101": ("Bahri's Special Soda", 1.75),
    "102": ("Bahri's Spicy Chips", 1.25),
    "103": ("Bahri's Smooth Chocolate Bar", 1.50),
    "104": ("Bahri's Chilled Water", 0.99),
    "105": ("Bahri's Fresh Fruit Juice", 2.50)
}

def display_menu():
    print("\nWelcome to Bahri's Snacks!")
    print("What would you like to enjoy today?")
    for code, (item, price) in menu.items():
        print(f"[Code {code}] {item}: ${price:.2f}")
    print("Type 'exit' anytime to leave.")

def dispense_change(amount_due, amount_paid):
    change = round(amount_paid - amount_due, 2)
    if change > 0:
        print(f"Here’s your change: ${change:.2f}. Don’t forget to grab it!")
    elif change == 0:
        print("Perfect payment! No change needed.")
    return change

def vending_machine():
    while True:
        display_menu()

        
        user_code = input("\nEnter the code of the item you’d like: ").strip()

        
        if user_code.lower() == 'exit':
            print("Thank you for visiting Bahri's Snacks! Have a wonderful day!")
            break

        
        if user_code not in menu:
            print("Invalid code. Please try again.")
            continue

        
        item_name, item_price = menu[user_code]
        print(f"You’ve chosen {item_name}, which costs ${item_price:.2f}.")

        
        try:
            user_payment = float(input("Please insert your payment: $"))
        except ValueError:
            print("Invalid payment input. Please enter a valid number.")
            continue

        if user_payment < item_price:
            print(f"Insufficient funds. {item_name} costs ${item_price:.2f}, but you only provided ${user_payment:.2f}.")
            print("Transaction canceled. Please try again.")
            continue

        
        print(f"Dispensing your {item_name}... Enjoy!")
        dispense_change(item_price, user_payment)

        
        another = input("Would you like to buy another item? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thanks for using Bahri's Snacks! See you next time!")
            break


if __name__ == "__main__":
    vending_machine()
