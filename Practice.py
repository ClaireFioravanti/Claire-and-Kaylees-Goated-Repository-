

decode_word = input("Enter a word to decode: ")
even = decode_word[:(len(decode_word) + 1) // 2]
odd = decode_word[(len(decode_word) + 1) // 2:]

decoded = ""

for i in range(len(odd)):
    decoded += even[i] + odd[i]

if len(even) > len(odd):
    decoded += even[-1]

print(decoded)