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

#conditional list comprehension

# new_list = [new_item for item in list if test]

names = ['Alex' , 'John' , 'Angela' , 'Bob' , 'Fardin' , 'Trixie']

short_name = [name for name in names if len(name) > 4]

print (short_name)

#squared number exercise

numbers_test = [1 , 1 ,2 , 3 ,5 ,8,13 ,21 , 34, 55]
squared_number = [num*num for num in numbers_test]

print(squared_number)


#even number exercise

even_numbers = [1 , 1 , 2 , 3 ,5 , 8 , 13, 21 , 34, 55]
result = [num for num in even_numbers if num % 2 == 0]

print(result)