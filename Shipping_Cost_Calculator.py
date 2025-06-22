def get_positive_float(prompt):
    """Helper function to get a positive float input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_shipping_cost(weight, rate):
    """Function to calculate the shipping cost."""
    return weight * rate

def main():
    """Main function to handle user interaction."""
    print("Welcome to the Shipping Cost Calculator!")
    
    # Get user inputs with validation
    weight = get_positive_float("Enter the package weight in kilograms: ")
    rate = get_positive_float("Enter the shipping rate per kilogram (USD): ")

    # Calculate the shipping cost
    shipping_cost = calculate_shipping_cost(weight, rate)

    # Display the result with formatting
    print(f"\nShipping Cost for {weight} kg at {rate} USD per kg: {shipping_cost:.2f} USD")

    # Option to calculate for another package
    while True:
        try_again = input("\nDo you want to calculate for another package? (y/n): ").lower()
        if try_again == 'y':
            main()  # Restart the program for new input
        elif try_again == 'n':
            print("Thank you for using the Shipping Cost Calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Run the program
if __name__ == "__main__":
    main()
