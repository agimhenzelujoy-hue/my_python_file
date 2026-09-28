numbers = input("Enter numbers without spaces: ")
reversed_number = ""
num_lenght = len(numbers)

for num in range(num_lenght -1, -1, -1):
    reversed_number += numbers[num]

print(reversed_number)




number = int(input("Enter numbers without spaces: "))
if number < 0:
    negative = True
    number = abs(number)
else:
    negative = False

reversed_number = 0

while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number = number // 10

if negative == True:
    reversed_number = reversed_number * -1
print(reversed_number)
