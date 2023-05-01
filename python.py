# 1.Write a Python function that takes two arguments (a and b) and returns their sum.

def addition(a,b):
    sum  = a+b
    return sum
print(addition(10,20))

# 3.Write a Python function that takes a list of integers as input and
# returns the sum of all the integers in the list.

def numbers(nums):
    return sum(my_numbers)

my_numbers = [10,20,40,50,90]
print(numbers("nums"))

# Write a Python function that takes a list of strings as input and 
# returns a new list with all the strings capitalized.

def capital(names):
     empty = []
     for name in names:
         return empty.append(name.capitalise())
names = ["cynthia","ishimwe","student"]
print (capital(names))

# Write a Python function that takes a list of integers as input and
# returns the highest value in the list.

def highest(elements):
    return max(elements)
elements = [10,30,80,67,45]
print(highest(elements))

# Write a Python function that takes a list of integers as input and
# returns a new list with all the even numbers removed.

def remove_even_numbers(numbs):
    empty = []
    for n in numbs:
        if n%2 != 0:
            empty.append(n)
    return empty
numbs = [10,20,67,45,37,17]
print(remove_even_numbers(numbs))

# Write a Python function that takes a string as input and returns the string reversed.

def reversed_string(country):
    county = "".join(reversed(country))
    return county
print (reversed_string("Rwanda"))