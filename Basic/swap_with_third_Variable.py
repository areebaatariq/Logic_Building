def get_number(prompt):
    while True:
        a = input(prompt)
        try:
            return float(a)
        except ValueError:
            print("Invalid number. Enter a valid number.")

# Get two numbers from the user
a = get_number("Please enter the first number: ")
b = get_number("Please enter the second number: ")

# Swap the numbers without using a third variable
a = a + b
b = a - b
a = a - b

# Output the swapped values
print(f"After swap without third variable, the numbers are: {a} {b}")
