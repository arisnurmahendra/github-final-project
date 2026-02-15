# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate
shipping_cost_eur = shipping_cost * 0.84

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
print(f"Shipping Cost: {shipping_cost_eur} EUR")

