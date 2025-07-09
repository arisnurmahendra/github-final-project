# Shipping Cost Calculator

## Input package weight and shipping rate
weight = None
while True:
    try:
        weight = float(input("Enter the package weight in kilograms: "))
        break
    except ValueError:
        print("Invalid Input. Please enter a valid weight: ")
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

