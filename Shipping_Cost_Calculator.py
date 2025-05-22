# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost_BT = weight * rate
shipping_efficiency = 0.85  # Assuming 85% efficiency in shipping
shipping_cost_AT = shipping_efficiency * shipping_cost_BT
## Display the result
print(f"Shipping Cost before TAX: {shipping_cost_BT} USD")
print(f"Shipping Cost after TAX: {shipping_cost_AT} USD")


