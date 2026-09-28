numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))

largest = max(numbers)
second_largest = None
for number in numbers:
    if number != largest:
        if second_largest is None or number > second_largest:
            second_largest = number
print("Second largest: ", second_largest)