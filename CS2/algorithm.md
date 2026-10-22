# Function Algoritms
1. Is index < length of list_items?

    a. strip the leading and trailing whitespace of the current item; list_items [index]

1. return the list list_items


"""
Purpose, parameters, and return value can be written in the code, but write what the algorithm does in 
"""

``` python 

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
print(wish(::3)) # Take every 3rd character

print(wish())




 

