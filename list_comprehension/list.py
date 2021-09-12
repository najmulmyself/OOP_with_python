# simple list looks like this

numbers = [1 , 2 , 3 , 4]
new_list = []

for n in numbers:
    add_list = n + 1
    new_list.append(add_list)


print (new_list)


# list comprehension code will do the same

numbers = [1 , 2 , 3 , 4, 5, 6]

new_numbers = [n+1 for n in numbers]
print (new_numbers)

# list comprehension formate :

# declare a list 

# new_variables = [new_item for item in list]

# Example 2

name = "Robot"

letter = [let for let in name]

print(letter)

# Example 3

range_list = [range*2 for range in range(7,12)]
print(range_list)