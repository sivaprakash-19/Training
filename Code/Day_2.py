
str1 = "Hello all"

print(str1.strip())    # Returns a string after removing all the trailing spaces in right and left.

print(str1.rstrip())    # Returns a string after removing all the trailing spaces in right.

print(str1.lstrip())    # Returns a string after removing all the trailing spaces in left.

str1 = str1.lower()   # Converts into a string of lowercase and returns a String. 

print(str1.isalnum())   # Checks if string is alphanumeric or not, if yes -> True, else -> False

print(str1.index("l"))  # Returns the first occurrence of substring in the string, if not present -> throws ValueError

print(str1.count("l"))  # Returns the count of sub strings present in string -> int 

print(str1[ : 5])   # Prints substring from start to 5, 5 is exclusive in nature
 
print(str1[2 : ]) # Prints substring from 2 to end of string, 2 is inclusive in nature

print(str1[0 : 3])  # Prints substring from 0 to 3, 3 is exclusive , 0 is inclusive in nature

print(str1[0])  # Print the character, at index 0
# str1[0] = "Hy"  # Cannot modify the contents, because strings are immutable 

print(str1)





'''
n = 10 & 8
print(n, type(n))
'''

'''
# Sets
nums = set()    # Creates an empty set
nums = { 20, 40, 20}
if 200 in nums : 
    print("Yes")
else : 
    print("No")

nums.add(70)    # Adds 70 to the set 
nums.discard(10) # Removes the element, if present, otherwise doesn't return any Error
nums.remove(10) # Removes element from set, if element not present -> KeyError
print(nums, type(nums))
'''


'''
# Creating a dictionary with key and value pairs
dict = {
    50 : 8,
    100 : 0,
}
if 10 in dict : 
    print("10 is present")
else :
    print("10 is not present")

for key in dict : 
    print(key, " : ", dict[key])

print("Before adding 50 : " , dict[50])
dict[50] = 10   # Adding an key value pair to dictionary, if key is present -> update the value, else -> create a new key value pair
print("After adding 50 : " , dict[50])
'''