# Global variables to store the inventory data and unit count
inventory = []

# Menu validation function: Handles user input and ensures only valid options (1-4) are selected


def menu_validation():
    print('\n---- Inventory Menu ----')
    print('1. Add product')
    print('2. Show inventory')
    print('3. Calculate statistics')
    print('4. Exit')
    try:
        menu_opt = int(input('\nChoose an option (1-4): '))
        if menu_opt in range(1, 5):
            return menu_opt
        print('\nError: Choose a valid option.')
        # Recursive call to keep the menu active on range error
        return menu_validation()
    except ValueError:
        print('\nError: Type an integer number.')
        # Recursive call to keep the menu active on type error
        return menu_validation()

# 1. Add product function: Requests, validates, and stores new products as dictionaries


def add_product(total_products):
    """Request data from the user and add a new dictionary to the inventory."""

    # Validate product name (letters only)
    while True:
        product_name = input('\nProduct name: ')
        if not product_name.isalpha():
            print('\nError: Product name can only contain letters')
        else:
            break

    # Validate price (positive floats)
    while True:
        try:
            product_price = float(input('Price: '))
            if product_price <= 0:
                print('\nError: Type a positive number:')
            else:
                break
        except ValueError:
            print('\nError: Type a number.')

    # Validate quantity (positive integers)
    while True:
        try:
            product_quantity = int(input('Quantity:'))
            if product_quantity <= 0:
                print('\nError: Type a positive number:')
            else:
                break
        except ValueError:
            print('\nError: Type an integer number.')

    # Create dictionary and update the global inventory list
    product = {'name': product_name,
               'price': product_price,
               'quantity': product_quantity
               }
    inventory.append(product)
    total_products += product_quantity
    print(f"\n{product_name} added.")
    return total_products

# 2. Show inventory function: Iterates through the list and displays each product


def show_inventory():
    if not inventory:
        print('\nEmpty inventory.')
    else:
        print("\n---- Current Inventory ----")
        for index, product in enumerate(inventory):
            # Formats price and quantity for readability
            total_per_product = product['price'] * product['quantity']
            print(
                f"{index+1}. Product: {product['name']} | Price: {product['price']:,.2f} | Quantity: {product['quantity']:,} | Total: {total_per_product:,.2f}")

# 3. Calculate statistics function: Performs basic math on the stored data


def calculate_statistics(total_products):
    """Calculates the total value and total registered units."""
    if not inventory:
        print('\nError: Cannot calculate statistics with an empty inventory.')
        return

    # Calculate total value by multiplying price * quantity for each entry
    inventory_total_value = 0
    for product in inventory:
        inventory_total_value += product['price'] * product['quantity']

    print('\n--- Inventory Statistics ---')
    print(f'Total Inventory Value: ${inventory_total_value:,.2f}')
    print(f'Total Registered Units: {total_products:,}')

# Main execution loop: Keeps the program running until the user chooses to exit


def main():
    """Main execution function using a match-case structure."""
    while True:
        option = menu_validation()

        match option:
            case 1:
                total_products = add_product(total_products=0)
            case 2:
                show_inventory()
            case 3:
                calculate_statistics(total_products)
            case 4:
                print('You\'ve exited successfully.')
                break


if __name__ == "__main__":
    main()

# WEEK OBJECTIVE SUMMARY:
# The goal this week was to implement a functional CRUD-style inventory system.
# Key concepts applied: modular functions, data persistence via lists of dictionaries,
# input validation loops, and basic arithmetic for business statistics.
