#Dictionary is nothing but a key:value pair

students = {
    'rob' : 1,
    'beck' : 2,
    'bob' : 3,
}


#update dictionary

students['beck'] = 2.0

# access key and value

print(students['rob'])
# print (students[3])
print (students)

# all keys accessing same as value with .values()

keys = students.keys()

print (keys)

#we can access key:value at the same time by .items()
#it returns a list 
item = students.items()
print (item)


#GENERAL DICTIONAR COMPREHENSION TEMPLATE 

# dict_variable = {key:value for item in list}

names = ['Alex' , 'John' , 'Angela' , 'Bob' , 'Fardin' , 'Trixie']
import random
scores = {student:random.randint(1,100) for student in names}
print (scores)

# dict_variable = {key:value for (key,value) in dictonary.items()}
# dict_variable = {key:value for (key,value) in dictonary.items() if test}

passed_scores = {student:scores for (student,scores) in scores.items() if scores > 30}
print (passed_scores)
