# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
dist = float(input("Enter the distance of the shipping in kilometers"))
## Calculate shipping cost
shipping_cost = weight * rate * dist

## Display the result
print(f"Shipping Cost is: {shipping_cost} USD")
