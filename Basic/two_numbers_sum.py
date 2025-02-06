# Prompt the user for the first and second numbers
first_input = input("Please enter the first number: ")
second_input = input("Please enter the second number: ")

try:
    # Convert the inputs to floats
    first_number = float(first_input)
    second_number = float(second_input)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    # Calculate the sum of the two numbers
    total = first_number + second_number
    # Print the result
    print(f"The sum of {first_number} and {second_number} is {total}.")
