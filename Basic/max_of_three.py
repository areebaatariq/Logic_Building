def get_number(prompt):
    while True:
        a = input(prompt)
        try:
            a = float(a)
            if a.is_integer():
                return int(a)
            else:
                print("Invalid number. Please enter an integer.")
        except ValueError:
            print("Invalid input. Enter a numerical value.")

def max_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Get three valid integer inputs from the user
a = get_number("Please enter the first number: ")
b = get_number("Please enter the second number: ")
c = get_number("Please enter the third number: ")

# Find and display the maximum number
max_value = max_number(a, b, c)
print(f"Max number among {a}, {b}, and {c} is {max_value}.")

# Use the built-in max function to find the maximum number
# max_value = max(a, b, c)
# print(f"Max number among {a}, {b}, and {c} is {max_value}.")
