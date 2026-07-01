import time

def hibachi_order():

    while True:   # Allows the customer to make another order

        # Menu
        menu = {
            "Chicken": 15.99,
            "Steak": 17.99,
            "Shrimp": 18.99,
            "Small Fried Rice": 3.99,
            "Large Fried Rice": 6.99,
            "Side Salad": 2.99,
            "Eel Avocado Sushi Roll": 7.99,
            "Gyoza": 14.99,
        }

        order_list = []
        total_bill = 0.00

        print("\nWelcome to Umami Hibachi Restaurant!")
        print("Type 'done' when you're finished ordering.")

        while True:
            print("\n------ MENU ------")
            for item, price in menu.items():
                print(f"{item}: ${price:.2f}")

            user_input = input("\nEnter your order: ").strip()

            if user_input.lower() == "done":
                break

            matched_item = None

        for item in menu:
            if user_input.lower() == item.lower():
                matched_item = item

        if matched_item:
            order_list.append(matched_item)
            total_bill += menu[matched_item]
            print(f"{matched_item} has been added to your order.")
        else:
            print("Sorry, that item is not on the menu.")

        # Receipt
        print("         RECEIPT")

        if len(order_list) == 0:
            print("No items ordered.")
        else:
            for item in order_list:
                print(f"{item:<30} ${menu[item]:.2f}")

        print("------------------------------")

        tax_rate = 0.06
        tax_amount = total_bill * tax_rate
        total = total_bill + tax_amount

        print(f"Subtotal: ${total_bill:.2f}")
        print(f"Tax (6%): ${tax_amount:.2f}")
        print(f"Total: ${total:.2f}")

        print("\nThank you for ordering!")


        # Ask if the customer wants to continue
        while True:
            choice = input("\nWould you like to place another order? (Y/N): ").strip().lower()

            if choice == "y":
                break

            elif choice == "n":
                print("\nThank you for visiting Umami Hibachi Restaurant!")
                time.sleep(3)   # Wait 3 seconds

                return

            else:
                print("Please enter Y or N.")


# Run the program
if __name__ == "__main__":
    hibachi_order()
