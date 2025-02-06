# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

 # Here is a new update by Dragana Neshevska
if shipping_cost > 100:
    discount = shipping_cost * 0.10  # 10% discount
    shipping_cost -= discount
    print(f"A 10% discount has been applied! New Shipping Cost: {shipping_cost:.2f} USD")

    

