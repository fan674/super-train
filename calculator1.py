🧮# Simple Calculator Program
# This program does basic math for you

# Function to add two numbers
def add(x, y):
    """Adds two numbers together"""
    return x + y

# Function to subtract two numbers  
def subtract(x, y):
    """Takes away second number from first number"""
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    """Multiplies two numbers together"""
    return x * y

# Function to divide two numbers
def divide(x, y):
    """Divides first number by second number"""
    # Check if we're trying to divide by zero
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"

# Main program starts here
print("🧮 Welcome to Simple Calculator!")
print("What do you want to do?")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (×)")
print("4. Divide (÷)")

# Get user's choice
choice = input("Pick a number (1, 2, 3, or 4): ")

# Get the two numbers from user
try:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
except ValueError:
    print("Please enter valid numbers only!")
    exit()

# Do the math based on user's choice
if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
    
elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
    
elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} × {num2} = {result}")
    
elif choice == '4':
    result = divide(num1, num2)
    if isinstance(result, str):  # If there's an error message
        print(result)
    else:
        print(f"{num1} ÷ {num2} = {result}")
        
else:
    print("Sorry, that's not a valid choice!")

print("Thanks for using the calculator! 👋")

