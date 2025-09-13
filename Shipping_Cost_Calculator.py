# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Optional: Ask for discount percentage
discount = float(input("Enter discount percentage (0 if none): "))

## Optional: Apply tax
tax_rate = 0.05  # 5% tax

## Calculate shipping cost
shipping_cost = weight * rate
discount_amount = shipping_cost * (discount / 100)
shipping_cost_after_discount = shipping_cost - discount_amount
final_cost = shipping_cost_after_discount * (1 + tax_rate)

## Display the result
print(f"Original Shipping Cost: {shipping_cost:.2f} USD")
print(f"Discount Applied: {discount_amount:.2f} USD")
print(f"Final Shipping Cost (with 5% tax): {final_cost:.2f} USD")
