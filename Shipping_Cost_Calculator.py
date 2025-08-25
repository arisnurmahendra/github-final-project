# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

shipping_cost_CAD = shipping_cost * 1.37

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
print(f"Shipping Cost in CAD: {shipping_cost_CAD} CAD")
