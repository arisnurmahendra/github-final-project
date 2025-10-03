# Shipping Cost Calculator
#   Edited one

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))

## Calculate shipping cost based on weight categories
if weight <= 2:
    rate = 5.00  # Standard rate for small packages
elif weight <= 10:
    rate = 3.50  # Reduced rate for medium packages
else:
    rate = 2.75  # Bulk rate for heavy packages

shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost:.2f} USD")
print(f"Applied Rate: {rate:.2f} USD per kg")