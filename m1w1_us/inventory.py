# Function to get user input and convert it to a specific type
# If the conversion fails, it prompts the user again (recursive)
def input_msg(message, value_type, msg_val_error=None):
    try:
        inp_value = value_type(input(message))  # Convert input to the specified type
        return inp_value
    except ValueError:
        print(msg_val_error)  # Print error message if conversion fails
        return input_msg(message, value_type, msg_val_error)  # Retry input recursively

# Function to get a valid product name (letters only, non-empty)
def get_product_name():
    """Prompt user for a valid product name (letters only, non-empty)."""
    product_name = input_msg('Enter the product name: ', str).strip()  # Get input and remove leading/trailing spaces
    if not product_name:
        print('Error: Name cannot be empty. Please try again.')
        return get_product_name()  # Retry if input is empty
    if not product_name.isalpha():
        print('Error: Name can only contain letters. Try again.')
        return get_product_name()  # Retry if input contains non-letter characters
    return product_name  # Return valid product name

# Function to get a valid product price (must be a positive float)
def get_product_price():
    """Prompt user for a valid product price (positive float)."""
    price = input_msg('Enter the product price: ', float, 'Error: Please enter a valid number for the price. Try again.')
    if price <= 0:
        print('Error: Price must be greater than 0. Try again.')
        return get_product_price()  # Retry if price is zero or negative
    return price  # Return valid price

# Function to get a valid product quantity (must be a positive integer)
def get_product_quantity():
    """Prompt user for a valid product quantity (positive integer)."""
    quantity = input_msg('Enter the product quantity: ', int, 'Error: Please enter a valid integer for the quantity. Try again.')
    if quantity <= 0:
        print('Error: Quantity must be greater than 0. Try again.')
        return get_product_quantity()  # Retry if quantity is zero or negative
    return quantity  # Return valid quantity

# Function to calculate total cost of the product
def calculate_total(price, quantity):
    """Calculate total cost for the product."""
    return price * quantity

# Function to display a formatted summary of product information
def display_summary(name, price, quantity, total):
    """Display a formatted summary of the product information."""
    print('\n----J. R. Store----')
    print(f'\nProduct: {name}')  # Display product name
    # :,.2f → formats the number as a float with 2 decimal places and adds commas as thousands separators
    print(f'\nPrice: {price:,.2f}')  # Display product price with 2 decimal places and comma as thousands separator
    print(f'Quantity: {quantity:,}')  # Display product quantity with comma as thousands separator
    print(f'Total: {total:,.2f}')  # Display total cost with 2 decimal places and comma separator

# Main function that runs the program
def main():
    """Main function to run the inventory program."""
    name = get_product_name().capitalize()  # Get and capitalize product name
    price = get_product_price()  # Get product price
    quantity = get_product_quantity()  # Get product quantity
    total = calculate_total(price, quantity)  # Calculate total cost
    display_summary(name, price, quantity, total)  # Show summary

# Check if this script is run directly (not imported), then run main
if __name__ == "__main__":
    main()