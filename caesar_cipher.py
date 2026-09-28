# a b c d e f g h i j k l m n o p q r s t u v w x y z
text = input("Enter a short text: ")

shift_number = int(input("Enter a shift number: "))

mode = input("Enter either 'encrypt' or 'decrypt': ")

result = ""

for char in text:

    if char.islower():

        if mode == "encrypt":
            shifted_char = chr((ord(char) - ord('a') + shift_number) % 26 + ord('a'))

        else:
            shifted_char = chr((ord(char) - ord('a') - shift_number) % 26 + ord('a'))

    elif char.isupper():

        if mode == "encrypt":
            shifted_char = chr((ord(char) - ord('A') + shift_number) % 26 + ord('A'))

        else:
            shifted_char = chr((ord(char) - ord('A') - shift_number) % 26 + ord('A'))

    else:
        shifted_char = char

    result += shifted_char

print(result)