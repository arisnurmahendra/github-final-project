# Shipping Cost Calculator
# Here is a new update by Corvert


## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
currency = input("Enter the currency (e.g., USD, EUR): ")

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} {currency}")
