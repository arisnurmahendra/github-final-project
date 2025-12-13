 # Here is a new update by <kerolbdu08-dev>
# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in ton: "))
rate = float(input("Enter the shipping rate per ton: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} MAD")

