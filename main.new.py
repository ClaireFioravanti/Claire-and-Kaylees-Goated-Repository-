phrase = "Robots are the best!"

#print the first character at index 0
print(phrase[0])
print(phrase[-20])

#print the length of the string. How many characters are there?
print(len(phrase))

#if we try to print character 20, there isn't actually a character at index 20
#print(phrase[20])

# print the last character of a string
print(phrase[len(phrase)-1])
print(phrase[-1])

wish = "My first class starts at 11:00 \t"
print(wish)

#String methods
print(wish.strip()) #strips the whitespace at the beginning and the end

lunch = " sandwich, chips, cauliflower, ginger ale " 
#print(lunch.split(','))
#split will take a string and create a list where it splits on the arument passed
#In this case, we split on a comma.

lunch_list = lunch.split(',')

#Write a functions that takes a list and strips off the leading and trailing
#whitespace of the items in the list

def strip_list(list_items):
    """
    Purpose: The function takes a list and strips leading and trailing whitespace from the items.

    Parameters: list_items - this is the list to be processed; list of strings

    Return Value: the list with whitespace removed

    """
    for index in range(len(list_items)):
        list_items[index] = list_items[index].strip()

    return list_items

lunch_list = strip_list(lunch_list)
print(lunch_list)

#Slicing
print(wish[0:5]) # the 1st character through the 4th character
print(wish[:5]) # same as above
print(wish[:8:3]) # Up to the 7th character and taking every 3rd character
print(wish[::3]) # Take every 3rd character






def username(first, last):
    '''
    Purpose: To create a username from the first and last names 
    of the form last_firstInitial. 

    Parameters: first - user's first name; str
    last - user's last name; str

    Return Value: the username of the form indicated in the description; str

    '''

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = last_name + "_" + first_name[0]
    return username 
    


def noVowels(text):
    
    '''
    Purpose: The vowels in the input string text are replaced with spaces.
    Parameters: text - the text where vowels are to be replaced; str
    Return Value: the string with the vowels replaced with spaces.
    '''

    '''
    Purpose: The vowels in the input string text are replaced with spaces.

    Parameters: text - the text where vowels are to be replaced; str

    Return Value: the string with the vowels replaced with spaces.
    '''

new_word = input("Enter a word to turn its vowels into spaces: ")
for letter in new_word:
    if letter.lower() in "aeiou":
        new_word = new_word.replace(letter, " ")
print(new_word)

def encode(harmony):

    '''
    Purpose: Encoding the parameter word where all even indexed characters
    are followed by all odd indexed characters. 

    Parameters: word - the text to be encoded; str

    Return Value: the encoded word

    '''

encode_word = input("Enter a word to encode: ")
even = encode_word[::2]
odd = encode_word[1::2]
print(even + odd)


def decode(mayrohn):
    '''
    Purpose: To undo the encode function.

    Parameters: word - the text to be decoded; str
    
    Return Value: the original word that was encoded.
    
    '''

decode_word = input("Enter a word to decode: ")
even = decode_word[:(len(decode_word) + 1) // 2]
odd = decode_word[(len(decode_word) + 1) // 2:]

decoded = ""

for i in range(len(odd)):
    decoded += even[i] + odd[i]

if len(even) > len(odd):
    decoded += even[-1]

print(decoded)



