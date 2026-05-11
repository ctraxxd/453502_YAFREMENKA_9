def average_even_numbers():
    """
    Calculate average of even numbers.
    Input ends when user enters 0.
    """
    total = 0
    count = 0

    while True:
        try:
            num = int(input("Enter integer (0 to stop): "))
        except ValueError:
            print("Invalid input!")
            continue

        if num == 0:
            break

        if num % 2 == 0:
            total += num
            count += 1

    if count == 0:
        print("No even numbers entered.")
    else:
        print("Average of even numbers:", total / count)
