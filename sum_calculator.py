# sum_calculator.py

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    # Example usage
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")
