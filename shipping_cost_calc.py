#The Logistics Shipping Cost Calculator.

#Enter the calculating factor function.

def shipping_cost_calc():
	"""Calculate the shipping cost based 
	on weight and shipping rate. 
	"""
	weight = float(input('Enter the Package Weight in kilogramme: '))
	rate = float(input('Enter the Package Shipping Rate per kilogramme: '))
	shipping_cost = weight * rate

	return shipping_cost

shipping_cost = shipping_cost_calc()
#Print the Shipping Cost
print(f'Shipping Cost: {shipping_cost}')


#Shipping Discount Feature
#Offering 10% Discount

if shipping_cost >200:
	discount = shipping_cost * 0.10
	shipping_cost -= discount
	print(f'Discount Applied: {discount}')
else:
	print('No Discount Applied. Better luck, next time!')

print(f'Final Shipping Cost: {shipping_cost}')