##text inside the quotes
print('hello world')

##variable argument inside the print function
message='hello world in single quote as variable'
print(message)

#to treat single code as normal char
#message='hello's world'
#SyntaxError: invalid syntax

#to avoid the above error we have to escape sinlge code using the escape char
message='hello\'s world'
print(message)

#insted of using escape char python has double quotes and triple quotes
message1="hello's world"
print(message1)

#triple quotes , we can extend text to new line also
message='''hello's world
welcome to "python world'''
print(message)

#to know the length of the string use this
print(len(message))
##output here is 38

#to access string at particular location use index
print(message[0])
#output is h, slice ranges from 0 to len-1

#if we try to access string index outside the range it will show error
#print(message[39])
#IndentationError: unexpected indent
#we can acess range also using slice,
#in the slice first index is inclusive and second index is exclusive
#last index ends with length-1
print(message1[0:5])

#from starting to 5th index
print(message1[:5])

#it will print from the 6th index to end of the string
print(message1[6:])
