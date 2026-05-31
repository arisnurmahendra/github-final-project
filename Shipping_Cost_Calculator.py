# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
location = int(input("Enter 1 for Sofia and 2 for province:"))

## Calculate shipping cost
shipping_cost = weight * rate * location

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

