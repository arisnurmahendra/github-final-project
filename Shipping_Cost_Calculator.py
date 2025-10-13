# Shipping Cost Calculator

def calculate_shipping_cost(weight, rate):
    """Calculates the shipping cost based on weight and rate.

    Args:
        weight (float): The weight of the package in kilograms.
        rate (float): The shipping rate per kilogram.

    Returns:
        float: The total shipping cost.
    """
    return weight * rate

def main():
    """Gets user input for package weight and shipping rate,
    calculates the shipping cost, and displays the result.
    """
    ## Input package weight and shipping rate
    weight = float(input("Enter the package weight in kilograms: "))
    rate = float(input("Enter the shipping rate per kilogram: "))

    ## Calculate shipping cost
    shipping_cost = calculate_shipping_cost(weight, rate)

    ## Display the result
    print(f"Shipping Cost: {shipping_cost} USD")

if __name__ == "__main__":
    main()
