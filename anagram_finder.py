first_word = input("Enter first word: ").lower()
second_word = input("Enter second word: ").lower()

first_frequency = {}
second_frequency = {}

for char in first_word:
    if char in first_frequency:
        first_frequency[char] += 1
    else:
        first_frequency[char] = 1
for char in second_word:
    if char in second_frequency:
        second_frequency[char] += 1
    else:
        second_frequency[char] = 1
if first_frequency == second_frequency:
    print("Anagrams")
else:
    print("Not an anagram")