# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

# Here is a new update by <bayramtturgutt>

def calculate_shipping_cost(weight, rate):
    return weight * rate

def main():
    try:
        # Input: package weight and shipping rate
        weight = float(input("Enter the package weight in kilograms: "))
        rate = float(input("Enter the shipping rate per kilogram (USD): "))
        
        # Calculate shipping cost
        shipping_cost = calculate_shipping_cost(weight, rate)
        
        # Output: Display the shipping cost
        print(f"Shipping Cost: {shipping_cost:.2f} USD")
    
    except ValueError:
        print("Invalid input! Please enter numerical values for weight and rate.")

if __name__ == "__main__":
    main()
