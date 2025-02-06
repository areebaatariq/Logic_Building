def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            # Convert the input to a float first.
            num = float(user_input)
            # Check if the float is actually an integer (e.g., 3.0 is acceptable).
            if num.is_integer():
                return int(num)
            else:
                print("Invalid number. Please enter an integer .")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def check_number(number):
    # Check if the number is even or odd.
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number_to_check = get_number("Please enter the number to check if it's even or odd: ")
result = check_number(number_to_check)
print(f"The number {number_to_check} is {result}.")
