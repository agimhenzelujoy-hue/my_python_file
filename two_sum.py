numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))
target = int(input("Enter your target number: "))
for first_number in range(len(numbers)):
    for second_number in range(first_number + 1, len(numbers)):
        if numbers[first_number] + numbers[second_number] == target:
            print(numbers[first_number], numbers[second_number])
            