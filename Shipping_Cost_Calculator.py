# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

def calculate_shipping(weight, distance, express=False):
    cost = (weight * 0.5) + (distance * 0.1)
    if express:
        cost += 20  # flat express fee
    return cost

# Example usage
print("Standard:", calculate_shipping(10, 100))
print("Express:", calculate_shipping(10, 100, express=True))