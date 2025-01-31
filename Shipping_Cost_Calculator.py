# Shipping Cost Calculator
 # Here is a new update by yardig-tech
git config --global user.email "188824178+yardig-tech@users.noreply.github.com"
git config --global user.name "yardig-tech"

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

