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
message1="Hello's World"
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

#to convert all letters to lower case letters
print(message1.lower())
##Hello's World to hello's world

#to convert all  letters to upper case letters
print(message1.upper())
##Hello's World to HELLO'S WORLD

#count take string as argument,World appers one time in the message variable
print(message1.count('World'))
##output is 1

#l appers three times in the message variable
print(message1.count('l'))
##output is 3

#find also takes string as argument, it gives at what indext it identifies the world
print(message1.find('World'))
##output 8, World starts at 8th index

#if we give input which could not find, then it gives the output -1
print(message1.find('universe'))
##output -1, because unviverse is not found in the string

#string replace won't happen in place
message2='Hello World'
message2.replace('World','Universe')
print(message2)
##output is Hello World, replacement did not happen
#Hello World

#for replacement compulsary we need to have retun statement
message2='Hello World'
new_message=message2.replace('World','Universe')
print(new_message)
#Hello Universe

#or to replace in the orginal message2 variable we need to give that variable in the left hand side
message2='Hello World'
message2=message2.replace('World','Universe')
print(message2)
#Hello Universe

#string concatination
messa='Hello'
messa1='World'
res=messa+messa1
print(res)
#output is HelloWorld

#string concatination to get some space
messa='Hello'
messa1='World'
res=messa+' '+messa1
print(res)
#output is Hello World

#string concatination one more example
greeting='Hello'
name='Hamsa'
mess=greeting+','+name+' Welcome!'
print(mess)
#output is Hello,Hamsa Welcome!

#string concatination if we have more variables then we have to follow like this
#imp here is no need +, also no need sigle quotes, one sigle quote for the whole.foramt
greeting='Hello'
name='Hamsa'
mess='{},{} Welcome!'.format(greeting,name)
print(mess)
#output is same Hello,Hamsa Welcome!



##in the latest python we have formtted strings, no need to use .format
greeting='Hello'
name='Hamsa'
mess=f'{greeting},{name} Welcome!'
print(mess)
#output is same Hello,Hamsa Welcome!

##with the formated strings easily we can do operations on strings
greeting='Hello'
name='Hamsa'
mess=f'{greeting.lower()},{name} Welcome!'
print(mess)
#output is  hello,Hamsa Welcome!

##dir(variable name), it prints all the functions and operations possiblw with that variable
##first line is methods, second line is operations
greeting='Hello'
name='Hamsa'
print(dir(name))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

##help(data type of variable name), it prints all the functions and operations possiblw with that variable
#following help display so many lines, it is difficult to read
##first line is methods, second line is operations
greeting='Hello'
name='Hamsa'
#print(help(str)) ##IT WILL HELP

#help(data type of variable name), it prints all the functions and operations possiblw with that variable
##using help , to get only reqired operation help we have to follow like this
greeting='Hello'
name='Hamsa'
print(help(str.lower))
#Help on method_descriptor:
#lower(self, /)
#    Return a copy of the string converted to lowercase.
#None
