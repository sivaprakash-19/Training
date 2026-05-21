
nums = (10,20,30)   # Tuple -> tuples are immutable, modifying is not possible. 
# Accessing all elements in tuple via forEach loop
for i in nums :
    print(i, end = " ")
# Iterative version of accessing elements in tuple
for i in range(len(nums)) : 
    print(i , ":", nums[i])
# nums[0] = 578 -> Not possible in tuple, because elements are immutable
print(nums.count(90))   # Count the number of times, element is present -> Returns int
print(nums.index(100)) # Returns the first occurrence of element, if not present throws ValueError -> Returns int
print(nums, type(nums))



'''
nums = [10,12,2,3,7,2,9] 
# Reverse the list without inbuilt functions
i = 0
j = len(nums) - 1
while i < j : 
    nums[i], nums[j] = nums[j], nums[i]
    i += 1
    j -= 1
print(nums)
'''

'''
def c() :
    print("Inside c")

def b() :
    c()
    print("Inside b")

def a() :
    b() 
    print("Inside a")

a() 
print("In line number 13")
b()
'''

'''
nums = [10,12,2,3]
nums.pop()  # Removes the last element, if list is empty throws IndexError
nums.remove(1) # Remove the first occurrence of the element, if element not present, throws ValueError
nums1 = nums.copy() # Creates a new list and copy all elements from original list
print(nums1)
nums.clear()    # Remove all the elements from list
nums.reverse() # Reverses the list 
nums1 = [90,80,70] 
nums.extend(nums1) # will add elements at last from object
nums.insert(10, 90) # Inserts element at index, then all elements from index -> rightShifted by 1 position, if index is not valid -> element will be inserted at last index
nums.append(567)    # Appends the element to the last
print(nums)
print(nums.index(100)) # If present, Returns the first occurence of element(int), else -> throw ValueError
print(nums.count(1))  # Returns the number of times, element is present in list (int)

# Accessing elements via index

for i in range(len(nums)) :
    print(i , " : ", nums[i])

# n = int(input("Enter number of elements : "))
# for i in range(n) : 
#     print("Enter ", i, " element : ", end = "")
#     num = int(input())
#     nums.append(num)

# nums.sort()

# Accessing elements via forEach loop
# for i in nums : 
#     print(i, end = " ")


# print(nums[-2], type(nums))

'''

'''
n = int(input("Enter n : "))
# First half
for i in range(1, n + 1) :
    # spaces -> n - i
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # stars -> 2 * i - 1
    for j in range(1, (2 * i)) : 
        print("*", end = " ")
    print()
# Second half
for i in range(n - 1, 0, -1) :
    # spaces -> n - i
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # stars -> 2 * i - 1
    for j in range(1, (2 * i)) : 
        print("*", end = " ")
    print()
'''

'''
end = (2 * n) - 1
for i in range(1, n + 1) :
    num = (2 * i) - 1 
    for j in range(1, n + 1) :
        print(num , end = " ")
        num += 2
        if num > end : 
            num = 1 
    print()
'''

'''
for i in range(1, n + 1) :
    # spaces -> n - i
    for j in range(1, n - i + 1): 
        print("_", end = " ")
    # stars -> i
    for j in range(1, i + 1) :
        print("*", end = " ")
    print()
'''
'''
for i in range(1, n) : 
    if i % 4 != 0 :
        print(i, end = " ")
'''

'''
for i in range(0, n, 2) :
    print(i , end = " ")

for i in range(n) :
    print(i , end = " ")

for i in range(0, n) :
    print(i , end = " ")
'''


'''
if n % 3 == 0 and n % 5 == 0 :
    print("Divisible by 3 and 5")
elif n % 3 == 0 :
    print("Divisible by 3")
elif n % 5 == 0 :
    print("Divisible by 5")
else :
    print("Not Divisible by 3 and 5")
'''

'''
if n > 100 : 
    print("Greater than 100")
elif n < 100 and n > 10 :
    print("Less than 100, greater than 10")
else :
    print("Less than 10")
'''

'''
if n % 2 == 1 :
    print(n , " is odd")
else :
    print(n , " is even")
    
print(n, type(n))
'''


'''
n = float(input("Enter n : "))
print("Value of n : ", n)
print(type(n))

a = False
print("Value of a : " , a)
print(type(a))
a = 10
print("Value of a : " , a)
print(type(a))


print("Good morning! Hope you're doing good", end = "+")
print("How are you??")
print("Hello")
'''