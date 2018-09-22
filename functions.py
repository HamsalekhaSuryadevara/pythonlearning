#functions is a block of stagements which need to execute repeatedly
#function keyword begins with the word def, follwoed by space after that closed brackes to pass the arguments


#without pass keyword if we run the function it will show below error
#IndentationError: expected an indented block
#def hello_fun():

#print(hello_fun())
#output is below error
#IndentationError: expected an indented block


#when we call(print) the function without parenthesis
#it just print the function exsistence in the memory
#it does not execute the function
def hello_fun():
    pass
print(hello_fun)
#output is <function hello_fun at 0x017BA588>, it means the hello_fun is a function in the memory at 0x0... location


#with the pass keword it returns None
def hello_fun():
    pass
print(hello_fun())
#output is None, because nothing is there to execute inside the function,,,but does not show error like above case




#here inside the function print statement is there so no need to call the function with the print statement
def hello_fun():
    print('hello_fun')
#print(hello_fun()), this is calling with the print statement
hello_fun()
#output is hello_fun


#without using functions, we are printing hello_fun 4 times
print('hello_fun!')
print('hello_fun!')
print('hello_fun!')
print('hello_fun!')
#output is hello_fun!
#hello_fun!
#hello_fun!
#hello_fun!



#in the above blcok of code we did not use the function
#if some one comes and ask insted of hello_fun!, we need hello_fun.
#then we need to chane in 4 places
#think of real progress if we need to modify something in 100's of lines code, it is very difficult to change in the all
#the 100'places, in this case function are very useful we just need to change only in one place
print('hello_fun.')
print('hello_fun.')
print('hello_fun.')
print('hello_fun.')
#output is hello_fun.
#hello_fun.
#hello_fun.
#hello_fun.



#function main pupose is the all the repeated set of instructions put to gether
#same above two blocks using functions
def hello_fun():
    print('hello_fun!')
hello_fun()
hello_fun()
hello_fun()
hello_fun()
#output is hello_fun!
#hello_fun!
#hello_fun!
#hello_fun!

##if we want to chane the ! to . using functions we just need to chane change in the one print statement, unlinke the case without
#using function
def hello_fun():
    print('hello_fun.')
hello_fun()
hello_fun()
hello_fun()
hello_fun()
#output is hello_fun.
#hello_fun.
#hello_fun.
#hello_fun.


#since we used return statement inside the function , we need to call the hello_fun with the print statement
def hello_fun():
     return 'hello_fun'
#print(hello_fun()), this is calling hello_fun inside the print statement
hello_fun()
#no output

#we should see the function as a machine(black box) which takes input, gives back the output
#ignore this line, tutor not told this line with the input(arguments), output(return)
#for example here length function takes string as input, returns integer
# we don't know the internals of the length function
#at the begging stage we don't need to know what is there inside the function
def hello_fun():
    pass
print(len('hamsa'))
#output is 5

##now lets understand the return
#retuns string it does not print anything by default when we call function
def hello_fun():
     return 'hello_fun'
hello_fun()
#no output

#to get the return value we should call the function inside the print
def hello_fun():
     return 'hello_fun'
#print(hello_fun()), this is calling hello_fun inside the print statement
print(hello_fun())
#output is hello_fun

##the advantage with the return statement, is we will get to know what type of data it i retunring
#here we know that it is retunring string , then we can use all the methods which works on strings
def hello_fun():
     return 'hello_fun'
#print(hello_fun()), this is calling hello_fun inside the print statement
print(hello_fun().upper())
#output is HELLO_FUN




##NOW LET US UNDERSTAND THE ARUMENTS
#if we give arguments in the function , but when we are calling if we don't give arguments
#then it will show error as required one positional argument
#def welcome(greeting):
    #return '{} well '.format(greeting)
#print(welcome())
#output error says welcome() missing 1 required positional argument: 'greeting'


#if we give arguments in the function , but when we are calling if we don't give arguments
#then it will show error as required one positional argument
#def welcome(greeting):
    #return '{} well '.format(greeting)
#print(welcome())
#output error says welcome() missing 1 required positional argument: 'greeting'


#function calling with the positional arguments
def welcome(greeting):
    return '{} well '.format(greeting)
print(welcome('ho'))
#output ho well

#we can have default arguments also, here if we give two arguments at calling function it take as it is
#if we give one argument at the calling function, then it will consider the defalt argument metioned at the
#called function
def welcome(greeting,name='lekha'):
    return '{} {} '.format(greeting,name)
print(welcome('hi'))
#output hi lekha

#if we are giving default argument at the calling function then we have to follow the order
#fisrt we have to give positional arguments , then we have to give keyword(default) arguments
#while giving default arguments at the calling function we have to follow same notation as
#the called function default argument
def welcome(greeting,name='lekha'):
    return '{} {} '.format(greeting,name)
print(welcome('hi', name='hamsa'))
#output hi hamsa

#we can give in random order the default and positional arguments using the concept of args, kwargs
#args(positional arguments), kwargs(keyword(default) arguments)
#*args,*kwargs, this is advanced topic
#output we get is, all the positional arguments as tuple
#all the keyword arguments as dictionary
# fisrt we have to give all positional arguments, then we have to give default arguments
def student(*args,**kwargs):
    print(args)
    print(kwargs)
student('maths','phy',name='hamsa',age=26)
#('maths', 'phy')
#{'name': 'hamsa', 'age': 26}



## we can give positional and default arguments seperately as below
## if call with the variable names then it gives output as below
#this is not what the output we are expecting
def student(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['maths','phy']
descr={'name':'hamsa','age':26}
student(courses,descr)
#(['maths', 'phy'], {'name': 'hamsa', 'age': 26})
#{}



## we can give positional and default arguments seperately as below
## at the calling function we have to give like as we gave at the called function, then the calling function
#will unpack those values
#but the meaning of *args,**kwargs, at the calling function and at the called function are different
def student(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['maths','phy']
descr={'name':'hamsa','age':26}
student(*courses,**descr)
#('maths', 'phy')
#{'name': 'hamsa', 'age': 26}



###small program covering all
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
#print(len(month_days))
def leaf_yr(year):
    return year%4==0 and (year%100!=0 or year%400==0)
#print(leaf_yr(2020)), return statement returns true if true, or false if False
def days_in_month(year, month):
    if not 1<=month<=12:
        print('invalid month')
print(days_in_month(2017,20))
#output for the above print statement
#output is invalid month





##small program covering all
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
#print(len(month_days))
def leaf_yr(year):
    return year%4==0 and (year%100!=0 or year%400==0)
#print(leaf_yr(2020)), return statement returns true if true, or false if False
def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'invalid month'
    if month==2 and leaf_yr(year):
        return 29
    return month_days[month]


print(days_in_month(2021,5))
#31
print(days_in_month(2021,2))
#28
