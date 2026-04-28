# Shipping Cost Calculator
def calculate_shipping(weight):
    if weight < 5:
        return 5
    else:
        return weight * 1.2
