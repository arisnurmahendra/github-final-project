# Shipping Cost Calculator

## Input package weight and shipping rate
## weight = float(input("Enter the package weight in kilograms: "))
## rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
## shipping_cost = weight * rate

## Display the result
## print(f"Shipping Cost: {shipping_cost} USD")

## I feel below will be a better coding for the calculator
"""
Shipping Logistics Rate Calculator

This script calculates shipping costs based on:
- Package weight
- Shipping distance (zone)
- Delivery speed (standard or express)
"""

from dataclasses import dataclass

# Base rates for shipping zones (distance-based)
ZONE_MULTIPLIERS = {
    "Zone 1": 1.0,   # Local
    "Zone 2": 1.5,   # Regional
    "Zone 3": 2.0,   # National
    "Zone 4": 2.5    # International
}

# Base rate per kg (can be configured)
BASE_RATE_PER_KG = 5.0

# Express surcharge (percentage)
EXPRESS_MULTIPLIER = 1.75

@dataclass
class Package:
    weight_kg: float
    zone: str
    express: bool = False

def calculate_shipping_cost(package: Package) -> float:
    if package.weight_kg <= 0:
        raise ValueError("Package weight must be greater than zero.")
    
    if package.zone not in ZONE_MULTIPLIERS:
        raise ValueError(f"Invalid shipping zone: {package.zone}")

    base_cost = BASE_RATE_PER_KG * package.weight_kg
    zone_multiplier = ZONE_MULTIPLIERS[package.zone]
    cost = base_cost * zone_multiplier

    if package.express:
        cost *= EXPRESS_MULTIPLIER

    return round(cost, 2)

# Example usage
if __name__ == "__main__":
    try:
        pkg = Package(weight_kg=2.5, zone="Zone 2", express=True)
        cost = calculate_shipping_cost(pkg)
        print(f"Shipping cost: ${cost}")
    except ValueError as e:
        print(f"Error: {e}")
