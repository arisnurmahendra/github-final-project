# Delivery Time Estimator
# Estimates delivery days based on distance and shipping type.

DELIVERY_SPEEDS = {
    "standard":  200,   # km per day
    "express":   500,
    "overnight": 1500,
}


def estimate_delivery_days(distance_km, shipping_type="standard"):
    """
    Estimate delivery time in days.

    Args:
        distance_km (float): Distance to destination in kilometers.
        shipping_type (str): One of 'standard', 'express', or 'overnight'.

    Returns:
        int: Estimated number of delivery days (minimum 1).
    """
    if shipping_type not in DELIVERY_SPEEDS:
        raise ValueError(f"Invalid shipping type. Choose from: {list(DELIVERY_SPEEDS.keys())}")
    if distance_km <= 0:
        raise ValueError("Distance must be greater than zero.")

    speed = DELIVERY_SPEEDS[shipping_type]
    days = max(1, -(-distance_km // speed))  # ceiling division
    return int(days)


if __name__ == "__main__":
    print("=== Delivery Time Estimator ===")
    try:
        distance = float(input("Enter shipping distance (km): "))
        shipping_type = input("Enter shipping type (standard/express/overnight): ").strip().lower()
        days = estimate_delivery_days(distance, shipping_type)
        print(f"Estimated delivery time: {days} day(s)")
    except ValueError as e:
        print(f"Error: {e}")
