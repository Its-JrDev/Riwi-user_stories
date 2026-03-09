# Program: Basic inventory registration with individual input validation
# Goal: Request product name, price, and quantity; calculate total cost and display results

# Request product name
while True:
    name = input('Enter the product name: ')  # Ask the user for the product name
    if name.strip() == "":                     # Check if the input is empty or only spaces
        print('Error: Name cannot be empty. Please try again.')
    elif not name.isalpha():                   # Check if the name contains only letters
        print('Error: Name can only contain letters. Try again')
    else: 
        break                                  # Exit loop if the name is valid

# Request product price
while True:
    try:
        price = float(input('Enter the product price: '))  # Ask the user for price and convert to float
        if price < 0:                                      # Price cannot be negative
            print('Error: Price cannot be negative. Please try again.')
        elif price == 0:                                   # Price cannot be zero
            print('Error: Price cannot be 0. Try again.')
        else:
            break                                         # Exit loop if the price is valid
    except ValueError:                                     # Catch non-numeric input
        print('Error: Please enter a valid number for the price. Try again.')

# Request product quantity
while True:
    try:
        quantity = int(input('Enter the product quantity: '))  # Ask the user for quantity and convert to int
        if quantity < 0:                                       # Quantity cannot be negative
            print('Error: Quantity cannot be negative. Please try again.')
        elif quantity == 0:                                    # Quantity cannot be zero
            print('Error: Quantity cannot be 0. Try again.')
        else:
            break                                             # Exit loop if the quantity is valid
    except ValueError:                                         # Catch non-integer input
        print('Error: Please enter a valid integer for the quantity. Try again.')

# Calculate total cost
total_cost = price * quantity                                  # Multiply price by quantity to get total cost

# Display results in console
print('\n----J. R. Store----')                                  # Header for the store
print(f'\nProduct: {name}')                                     # Display product name
print(f'\nPrice: {price} \nQuantity: {quantity}')              # Display price and quantity
print(f'\nTotal: {total_cost}')                                   # Display total cost

# End of program
# This program asks the user for a product name, price, and quantity,
# validates each input separately using loops and try/except,
# calculates the total cost, and prints a clear summary in the console.