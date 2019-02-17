#TUPLES
#Tuple-sequence of immutable python objects.
#Tuples are sequences, just like lists.
#Round brackets are used instead of square brackets in tuples.
#Both no.s & text can be typed in tuple unlike lists (only 1).
#We can't append anything to tuples.
#DICTIONARY
#Dictionary is a set of key- value pairs.
#Each key is seperated from its value by a colon(:),the items are separated by commas(,).

a={1:"number one", 22:"number twenty two"}
print(a)
print(a[1])
print(a[22])

dict_employee = {'Employee_name': 'Ramu', 'Age': 34, 'Designation': 'Software engineer'}
print(dict_employee)

dict_employee['Employee_name']="Ramu Karvi"
dict_employee['Designation']="Software engineer"
print(dict_employee)
#del dict_employee['Age']
#dict employee.clear()
print(dict_employee.items())
print(len(dict_employee))
dict_employee.update({"hometown":"Hyderabad"})
dict_employee.update({"Age":35})
print(dict_employee)

#concatenation
#del
#clear
#items
#keys
#values
#len()
#update

import random
print(random.randint(1,10))

#hw-write a python script which generates a random number between 0 & 13. Also check if it's prime or not.
#json="JavaScript Object Notation"
#Dict is a data type in python which u can just able to use in python, json is not an data type or object.

import json
x='{"name":"John","age":30,"city":"New York"}'
type(x)

y=json.loads(x)
type(y) #The result y is a Python dictionary:

print(y["age"])