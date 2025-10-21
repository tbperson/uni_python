
menu = [["Cheese_and_tomato", 6.00],
        ["Pepperoni_and_mozzarella", 8.50],
        ["Bacon_and_cheese", 9.25],
        ["Chicken_and_mushroom", 9.00],
        ["Hawaiian", 7.25]]

def calculate_delivery_charge(distance):
    if distance <= 1:
        return 0.0
    elif distance <= 3:
        return 3.0
    elif distance <= 6:
        return 6.0
    elif distance > 6:
        return 99999.0


def show_menu():
    print("Menu:")
    for index, (pizza, price) in enumerate(menu, start=1):
        print(f"{index}. {pizza} - £{price:.2f}")


def select_items():
    subtotal = 0.0
    show_menu()
    while True:
        choice = input("Enter the number of the pizza you want to order, or 'end' to finish: ")
        if choice.lower() == 'end':
            return subtotal
        elif choice.isdigit() and 1 <= int(choice) <= len(menu):
            pizza_index = int(choice) - 1
            subtotal += menu[pizza_index][1]
        else:
            print("Invalid choice. Please try again.")


def main():

    delivery_charge = calculate_delivery_charge(float(input("Enter delivery distance in miles: ")))
    if delivery_charge == 99999.0:
        print("Sorry, we do not deliver to this address.")
        return

    subtotal = select_items()

    total = subtotal + delivery_charge    
    print(f"Subtotal: £{subtotal:.2f}")
    print(f"Delivery Charge: £{delivery_charge:.2f}")
    print(f"Total: £{total:.2f}")

if __name__ == "__main__":
    main()
