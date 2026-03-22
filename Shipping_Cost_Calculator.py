# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Input destination distance
distance = float(input("Enter the shipping distance in kilometers: "))

## Calculate shipping cost with distance surcharge
BASE_FEE = 5.00
distance_surcharge = 0.01 * distance  # $0.01 per km
shipping_cost = BASE_FEE + (weight * rate) + distance_surcharge

## Display the result
print(f"Base Fee:           $5.00")
print(f"Weight/Rate Cost:   ${weight * rate:.2f}")
print(f"Distance Surcharge: ${distance_surcharge:.2f}")
print(f"Total Shipping Cost: ${shipping_cost:.2f} USD")

