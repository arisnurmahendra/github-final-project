# Shipping Cost Calculator

## Input package weight and shipping rate
while True:
    
    try:
        weight = float(input("Enter the package weight in kilograms: "))
        if weight > 0:
            break
        else:
            print('The value must be a number')
    except ValueError:
        print("Invalid input: it must be a number")
            
while True:
    
    try:
        rate = float(input("Enter the shipping rate per kilogram: "))
        if rate > 0:
            break
        else:
            print('The value must be a number')
    except ValueError:
        print("Invalid input: it must be a number")

        

    

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

