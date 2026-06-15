# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print("\n=== Shipping Cost Summary ===")
print(f"Package Weight: {weight} kg")
print(f"Shipping Rate: {rate} USD/kg")
print(f"Shipping Cost: {shipping_cost:.2f} USD")

