# Here is a new update by  Gabriel Flores on the Shipping Cost Calculator. This program calculates the shipping cost based on the weight of the package and the shipping rate per kilogram.
# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

