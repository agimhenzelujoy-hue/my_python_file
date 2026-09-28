word = input("Enter word: ").lower()
reverse_word = ""
word_length = len(word)

for index in range(word_length-1, -1, -1):
    reverse_word += word[index]

print(reverse_word)

if word == reverse_word:
    print(f"Output : {word} is a palindrome")
else:
    print(f"Output: {word} is not a palindrome")