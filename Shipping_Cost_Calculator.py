# Shipping Cost Calculator

SHIPPING_RATES = {
    "standard":  {"rate_per_kg": 2.5,  "base_fee": 5.0,  "days": "5-7"},
    "express":   {"rate_per_kg": 5.0,  "base_fee": 10.0, "days": "2-3"},
    "overnight": {"rate_per_kg": 10.0, "base_fee": 20.0, "days": "1"},
}

DISTANCE_MULTIPLIER = {
    "local":         1.0,
    "regional":      1.5,
    "international": 3.0,
}

def calculate_shipping(weight_kg, shipping_type, distance_zone):
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")
    if shipping_type not in SHIPPING_RATES:
        raise ValueError(f"Invalid shipping type. Choose from: {list(SHIPPING_RATES.keys())}")
    if distance_zone not in DISTANCE_MULTIPLIER:
        raise ValueError(f"Invalid distance zone. Choose from: {list(DISTANCE_MULTIPLIER.keys())}")

    rate = SHIPPING_RATES[shipping_type]
    multiplier = DISTANCE_MULTIPLIER[distance_zone]
    cost = round((rate["base_fee"] + rate["rate_per_kg"] * weight_kg) * multiplier, 2)

    return {
        "cost": cost,
        "estimated_delivery": f"{rate['days']} business days",
    }

def main():
    print("Welcome to the Shipping Calculator!")
    print("------------------------------------")
    try:
        weight = float(input("Enter package weight (kg): "))
        print(f"Shipping types: {', '.join(SHIPPING_RATES.keys())}")
        shipping = input("Enter shipping type: ").strip().lower()
        print(f"Distance zones: {', '.join(DISTANCE_MULTIPLIER.keys())}")
        zone = input("Enter distance zone: ").strip().lower()

        result = calculate_shipping(weight, shipping, zone)
        print("\n========== Shipping Quote ==========")
        print(f"  Cost    : ${result['cost']:.2f}")
        print(f"  Delivery: {result['estimated_delivery']}")
        print("====================================\n")

    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()