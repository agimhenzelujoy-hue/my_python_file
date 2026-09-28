sentence = input("Enter a short sentence: ").lower()
punctuation = "!@#~`$%^&*.'"
for character in punctuation:
    sentence = sentence.replace(character, "")
words = {}
for word in sentence.split():
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for key, value in words.items():
    print(f"{key}: {value}")