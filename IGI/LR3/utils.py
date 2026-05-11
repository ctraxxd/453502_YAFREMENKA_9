"""
Lab Work №3
Theme: Standard data types, collections, functions, modules
Version: 1.0
Developer: Ivanov Ivan Ivanovich
Date: 06.05.2026
"""

def repeat_program(func):
    """
    Decorator for repeating program execution.
    """
    def wrapper():
        while True:
            func()
            answer = input("\nDo you want to continue? (y/n): ").lower()
            if answer != 'y':
                print("Program finished.")
                break
    return wrapper


def input_float(message):
    """
    Safe float input with error handling.
    """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def input_int(message):
    """
    Safe integer input with error handling.
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input! Please enter an integer.")