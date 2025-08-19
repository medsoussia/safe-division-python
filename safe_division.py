# ===============================
# Python Project: Safe Division
# Features:
# - Safe user input (integers only)
# - Error handling (try/except)
# - List operations
# - Division with ZeroDivisionError handling
# - Table-like output for readability
# ===============================

def read_positive_int(prompt):
    """
    Ask the user to enter a positive integer.
    Repeat until the user enters a valid number > 0.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def read_numbers(n):
    """
    Read 'n' integers from the user and return them as a list.
    """
    numbers = []
    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: ").strip())
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return numbers

def divide_numbers(numbers):
    """
    Ask for a denominator and divide each number in the list by it.
    Handles division by zero and invalid input.
    """
    while True:
        try:
            denominator = int(input("Enter the denominator: ").strip())
            results = [num / denominator for num in numbers]
            
            # Table-like output
            print("\nDivision Results:")
            print(f"{'Number':>10} | {'Denominator':>12} | {'Result':>10}")
            print("-" * 38)
            for num, res in zip(numbers, results):
                print(f"{num:>10} | {denominator:>12} | {res:>10.2f}")
            break
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Safe Division Program!")
    n = read_positive_int("How many numbers do you want to enter? ")
    numbers = read_numbers(n)
    divide_numbers(numbers)
    print("\nAll numbers divided successfully!")

if __name__ == "__main__":
    main()
