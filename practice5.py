# Author: Kayla Wells
# Practice : 5
# Date: 2/5/26
# Description: Sum and average and minimum and maximum number generator
#
# Sample Run:
#
# Welcome to the Fun Stats Program!
# Type in one integer at a time and input 0 when you are finished.
# Enter an integer: 8
# Enter an integer: 23
# Enter an integer: 5
# Enter an integer: 0
#
# Results:
# Sum: 36
# Average: 13
# Minimum: 5
# Maximum: 23
#
# Would you like to run the program again? (y/n): n
# Good luck and have a great day!

def main():
    run_again = "y"

    while run_again == "y":
        print("Welcome to the Fun Stats Program!")
        print("Type in one integer at a time and input 0 when you are finished.")

        numbers = []
        user_number = get_number()

        while user_number != 0:
            numbers.append(user_number)
            user_number = get_number()

        total = calculate_sum(numbers)
        average = calculate_average(numbers)
        minimum = find_min(numbers)
        maximum = find_max(numbers)
        display_results(total, average, minimum, maximum)

        run_again = input("Would you like to run the program again? (y/n): ")

    print_goodbye()

def get_number():
    """Prompt the user to enter a number.
    parameters: none
    returns: number
    """
    number = int(input("Enter an integer: "))
    return number

def calculate_sum(numbers):
    """calculates the sum of list of numbers.
    parameters: list of numbers
    returns: sum of numbers
    """
    total = sum(numbers)
    return total

def calculate_average(numbers):
    """calculates the average of list of numbers.
    parameters: list of numbers
    returns: average of numbers
    """
    average = sum(numbers) / len(numbers)
    return average

def find_min(numbers):
    """finds the smallest number in list of numbers.
    parameters: list of numbers
    returns: smallest number
    """
    minimum = min(numbers)
    return minimum

def find_max(numbers):
    """finds the largest number in list of numbers.
    parameters: list of numbers
    returns: largest number
    """
    maximum = max(numbers)
    return maximum

def display_results(total, average, minimum, maximum):
    """displays the results of the calculation.
    parameters: total, average, minimum, maximum
    returns: results
    """
    print("\nResults:")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

def goodbye
    print("Good luck and have a great day!")

main()

