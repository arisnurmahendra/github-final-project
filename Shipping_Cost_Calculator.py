# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))
distance = float(input("Enter the shipping distance in kilometers: "))

## Validate inputs
if weight <= 0 or rate <= 0 or distance <= 0:
    print("Error: All values must be greater than zero.")
else:
    ## Calculate shipping cost
    shipping_cost = (weight * rate) + (distance * 0.1)

    ## Estimate delivery days
    if distance < 100:
        delivery_days = 1
    elif distance < 500:
        delivery_days = 3
    else:
        delivery_days = 7

    ## Display the result
    print(f"Shipping Cost: {shipping_cost:.2f} USD")
    print(f"Estimated Delivery: {delivery_days} days")