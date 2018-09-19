#dictionary is a key value pair, where key is unique-immutable
#value is anything
#key and value can be of any data type , where key is immutable
#key is like word in dictionary, value is like meaning for the world
#lets take student dictionary
#key and value are seperated by column
student={'name':'john','age':25,'courses':['maths','comsci']}
print(student)
#output is {'name': 'john', 'age': 25, 'courses': ['maths', 'comsci']}

#to acees only particular key , get that value, insted of whole dictionary
print(student['name'])
#output is john

#if we access key that is not included in dictionary
#print(student['phone'])
#KeyError: 'phone'
#but if we access using get method, if the key does not exsist it returs none, or even we can set the default value
print(student.get('phone'))
#output is None

##setting default value for the key which is not exsist in the dictionary
print(student.get('phone','Not present'))
#output is Not present

##we can include key values in the dictionary like this, here 555-4455 should be included in single quotes
student['phone']='555-4455'
print(student['phone'])
#555-4455
print(student.get('phone'))
#555-4455

#if we want to update the values in the dictionary
student['name']='jane'
student['age']=26
print(student)
#{'name': 'jane', 'age': 26, 'courses': ['maths', 'comsci'], 'phone': '555-4455'}

#insted of using multiple lines like above to update the dictionary,we can update the dictionary in the single line
student.update({'name':'hamsa','age':27,'phone':'555-3453'})
print(student)
#{'name': 'hamsa', 'age': 27, 'courses': ['maths', 'comsci'], 'phone': '555-3453'}

#to remove the element from the dictionary
del student['age']
print(student)
##in this dictionary age is deleted {'name': 'hamsa', 'courses': ['maths', 'comsci'], 'phone': '555-3453'}

#to remove the element from the dictionary, like a list we can use pop method also
#pop method keep the removed values in the return variable, return variable here is left handside variable
student['age']=26
age=student.pop('age')
print(student)
print(age)
##in this dictionary age is deleted {'name': 'hamsa', 'courses': ['maths', 'comsci'], 'phone': '555-3453'}
#age is 26

#to get length of dictionary
print(len(student))
#3

#to get only keys in the dictionary
print(student.keys())
#output is dict_keys(['name', 'courses', 'phone'])

#to get only values in the dictionary
print(student.values())
#output is dict_values(['hamsa', ['maths', 'comsci'], '555-3453'])

#to get both key and values from the dict_keys we need to use item method
print(student.items())
#dict_items([('name', 'hamsa'), ('courses', ['maths', 'comsci']), ('phone', '555-3453')])

##loop through of dictionary is bit different compared to lists
for key in student:
    print(key)
#name
#courses
#phone

##loop through of dictionary is bit different compared to lists
for value in student:
    print(value)
#name
#courses
#phone

#so if we simply access the dictionary like above it gives only one value
for key,value in student.items():
    print(key,value)
#name hamsa
#courses ['maths', 'comsci']
#phone 555-3453
