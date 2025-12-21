# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
pkg = int(input("Enter the package number: "))

## Calculate shipping cost
shipping_cost = (pkg*weight)*rate

## Display the result
print(f"Shipping Cost: ${shipping_cost:,.2f} USD")

