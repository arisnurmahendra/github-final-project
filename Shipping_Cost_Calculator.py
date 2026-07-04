# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms(kg): "))
rate = float(input("Enter the shipping rate per kilogram (USD/kg): "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"The cost of shipping for a {weight} kg package at ${rate}/kg is: ${shipping_cost:.2f} USD")

