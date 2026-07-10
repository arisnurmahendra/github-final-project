# Shipping Cost Calculator
# Here is a new update by gabrielcji 2

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kgs.: "))
rate = float(input("Enter the shipping rate per kg.: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

