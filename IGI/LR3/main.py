from utils import repeat_program, input_float
from task1 import arccos_series
from task2 import average_even_numbers
from task3 import count_spaces_punctuation
from task4 import analyze_string
from task5 import process_list

@repeat_program
def main():
    """
    Main menu for Lab Work №3 Variant 9
    """
    print("\n--- LAB WORK 3 ---")
    print("1 - Task 1 (Series)")
    print("2 - Task 2 (Cycle)")
    print("3 - Task 3 (Text)")
    print("4 - Task 4 (String analysis)")
    print("5 - Task 5 (List processing)")

    choice = input("Choose task: ")

    if choice == '1':
        x = input_float("Enter x (-1 to 1): ")
        eps = input_float("Enter eps: ")

        try:
            result, n, math_result = arccos_series(x, eps)
            print(f"x = {x}")
            print(f"n = {n}")
            print(f"F(x) = {result}")
            print(f"Math F(x) = {math_result}")
            print(f"eps = {eps}")
        except ValueError as e:
            print(e)

    elif choice == '2':
        average_even_numbers()

    elif choice == '3':
        count_spaces_punctuation()

    elif choice == '4':
        analyze_string()

    elif choice == '5':
        process_list()

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()