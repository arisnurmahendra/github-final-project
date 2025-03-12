def calculate_shipping_cost(weight, distance):
    """
    Calculate the shipping cost based on weight and distance.
    """
    base_cost = 50  # Base cost in dollars

    # Additional cost per kilogram
    weight_cost = 20 * weight

    # Additional cost per kilometer
    distance_cost = 5 * distance

    # Total cost calculation
    total_cost = base_cost + weight_cost + distance_cost
    return total_cost


def main():
    try:
        weight = float(input("Enter the package weight (in kg): "))
        distance = float(input("Enter the shipping distance (in km): "))

        # Validate inputs
        if weight <= 0 or distance <= 0:
            print("Weight and distance must be positive numbers.")
            return

        cost = calculate_shipping_cost(weight, distance)
        print(f"Total shipping cost: ${cost:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()
