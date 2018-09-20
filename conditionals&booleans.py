#if block
if True:
    print('condition  true' )
#output is condition  true

if False:
    print('condition  true' )
#no output

##if else block
language='python'
if language=='python':
    print('language is python' )
else:
    print('nothing')
#output is language is python

language='java'
if language=='python':
    print('language is python' )
else:
    print('nothing')
#output is nothing

#to test java presence as well in python we have elif statement
language='java'
if language=='python':
    print('language is python' )
elif language=='java':
    print('language is java' )
else:
    print('nothing')
#output is language is java

#in python switch statement is not exsist, because if-elif---else do same function as switch
language='javascript'
if language=='python':
    print('language is python' )
elif language=='java':
    print('language is java' )
elif language=='javascript':
    print('language is javascript' )
else:
    print('nothing')
#output is language is javascript

#boolean operations in python
#and,or,not
#and example
username='hamsa'
loggin=True
if username=='hamsa' and loggin:
    print('admin page')
else:
    print('not valid creds')
#output is admin page

#another example for and when one condition was False
username='hamsa'
loggin=False
if username=='hamsa' and loggin:
    print('admin page')
else:
    print('not valid creds')
#output is not valid creds

#same above code executes for or example
username='hamsa'
loggin=False
if username=='hamsa' or loggin:
    print('admin page')
else:
    print('not valid creds')
#output is not admin page

#not example
username='hamsa'
loggin=False
if not loggin:
    print('please login again ')
#please login again

#is operator compares the address(weather to objects has same address in memory) in python
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a is b)
#output
#25250352
#25616216
#False

#here both objects has same id, same address in memory
#3rd and 4th print statements are same
a=[1,2,3]
b=a
print(id(a))
print(id(b))
print(a is b)
print(id(a)==id(b))
#output
#10935192
#10935192
#True
#True

#True and False cases in python
#all the below are most common False cases, except(remaining) all are True
#False
#None
#zero of any numeric type
#empty srting,list,tuple-'',[],()
#empty mapping, means empty dictionary {}
condition=False
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is false

#None case
condition=None
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is false


#except zero, remaining any digits evaluates to True
condition=10
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is true

#empty string evaluates to false
condition=''
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is false

#empty list evaluates to false
condition=[]
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is false

#empty dictionary evaluates to false
condition={}
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is false

#other than empty things remaining all evaluates to true, following  example is for
#non empty string
condition='non empty'
if condition:
    print('condition is true')
else:
    print('condition is false')
#condition is true
