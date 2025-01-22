# Shipping Cost Calculator
def shipping_cost_calculator(weight, rate):
    """
    Calculates the shipping cost for a given package weight and rate.

    Parameters
    ----------
    weight : float
        The package weight in kilograms.
    rate : float
        The shipping rate per kilogram.

    Returns
    -------
    float
        The shipping cost in US dollars.
    """
    return weight * rate


## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = shipping_cost_calculator(weight, rate)

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
