# Shipping Cost Calculator (Updated Version)

weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Adding basic validation
if weight <= 0 or rate <= 0:
    print("Weight and rate must be positive numbers.")
else:
    shipping_cost = weight * rate
    print(f"Shipping Cost: {shipping_cost} USD")
# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

