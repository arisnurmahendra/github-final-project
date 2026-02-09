# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Validate input
if weight <= 0 or rate <= 0:
    print("Weight and rate must be positive numbers.")
else:
    # Calculate shipping cost
    shipping_cost = weight * rate

    # Display the result
    print(f"Shipping Cost: {shipping_cost:.2f} USD")

    #this is an update
