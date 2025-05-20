# Shipping Cost Calculator - Enhanced Version

def calculate_shipping():
    """Calculate shipping cost based on weight and rate"""
    print("\n=== Shipping Cost Calculator ===")
    
    # Get user input with validation
    while True:
        try:
            weight = float(input("Enter package weight (kg): "))
            rate = float(input("Enter shipping rate per kg (USD): "))
            if weight <= 0 or rate <= 0:
                print("Error: Values must be positive numbers")
                continue
            break
        except ValueError:
            print("Error: Please enter numbers only")

    # Calculate and display
    shipping_cost = weight * rate
    print(f"\nShipping Cost: {shipping_cost:.2f} USD")

if __name__ == "__main__":
    calculate_shipping()