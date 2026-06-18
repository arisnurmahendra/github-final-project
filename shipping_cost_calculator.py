def calculate_shipping_cost(weight):
    if weight<= 5:
        return 5
    elif weight <= 10:
        return 10
    else:
        return 20
print(calculate_shipping_cost(7))
