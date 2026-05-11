def process_list():
    """
    Find:
    1) product of negative elements
    2) sum of positive elements before maximum element
    """

    size = int(input("Enter list size: "))
    numbers = []

    for i in range(size):
        while True:
            try:
                num = float(input(f"Enter element {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input!")

    print("List:", numbers)

    # product of negative elements
    product = 1
    has_negative = False
    for num in numbers:
        if num < 0:
            product *= num
            has_negative = True

    if not has_negative:
        product = 0

    # sum before maximum
    max_value = max(numbers)
    index = numbers.index(max_value)

    sum_before = sum(numbers[:index])

    print("Product of negative elements:", product)
    print("Sum before maximum element:", sum_before)