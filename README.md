# Project Overview

The Hibachi Ordering System is a Python console application that simulates a simple restaurant ordering experience. It allows customers to choose food items from a menu, keeps track of their order, calculates the total cost with tax, prints a receipt, and lets them decide whether to place another order or exit the program.

# What can it do?
The Hibachi Ordering System includes the following features:

- Displays a menu containing available hibachi meals, side dishes, and their prices.
- Allows customers to enter multiple food items during one order.
- Checks whether the item entered by the customer exists on the menu before adding it.
- Stores all selected menu items in an order list.
- Calculates the subtotal based on all selected items, a 6% sales tax automatically, and displays the final total cost.
- Prints a receipt showing every item ordered, the subtotal, tax, and total amount due.
- Allows the customer to begin a completely new order without restarting the program.
- Displays a thank-you message before closing the application when the customer chooses to exit.

# Controls

To add a menu item to your order, type the name of the food exactly as it appears on the menu, such as Chicken, Steak, or Shrimp, and press Enter. If the item is available, the program will add it to your order and display a confirmation message.

When you have finished selecting all of your food items, type done and press Enter. The program will stop accepting new menu items and print a receipt showing everything you ordered, along with the subtotal, sales tax, and final total.

After the receipt is displayed, the program will ask if you would like to place another order. Type Y and press Enter if you want to start a new order. This will return you to the main ordering menu so you can place another order without restarting the program.

If you are finished using the application, type N and press Enter. The program will display a thank-you message, wait for three seconds, and then automatically close.
