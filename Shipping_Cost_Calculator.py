# Shipping Cost Calculator

## Input package weight and shipping rate
#weight = float(input("Enter the package weight in kilograms: "))
#rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
#shipping_cost = weight * rate

## Display the result
##print(f"Shipping Cost: {shipping_cost} USD")

def calculate_tax(cost, tax_rate=0.08):
    """Calcula el impuesto basado en el costo del envío."""
    return cost * tax_rate
def calculate_shipping_cost(weight, distance, transport_mode):
    """Calcula el costo de envío basado en peso, distancia y modo de transporte."""
    base_rate = 5.0  # Tarifa base en USD
    cost_per_kg = 2.0  # Costo por kilogramo
    cost_per_km = 0.1  # Costo por kilómetro
    base_cost = base_rate + (weight * cost_per_kg) + (distance * cost_per_km)
    tax = calculate_tax(base_cost)
    return base_cost + tax
