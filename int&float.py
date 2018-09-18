num=4
print(type(num))
#output is <class 'int'>

#Arithmetic operations
#ADDTION      3+2
#SUBTRACTION  3-2
#MUL          3*2
#DIV          3/2
#FLOOR DIV    3//2
#EXPONET      3**2
#MODULUS      3%2
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)
print(3**2)
print(3%2)
#output is as below
#5
#1
#6
#1.5
#1
#9
#1

print(2%2)
print(3%2)
print(4%2)
print(5%2)
print(6%2)
##output for the avove print cmds
#1
#0
#1
#0
#1
#0
print(3*2+1)
#7
print(3*(2+1))
#9

#increment in python
num=1
num=num+1
print(num)
#2

#short hand increment in python
num=2
num+=1
print(num)
#3

##like in simlilar way as addition, we can use -,*,,,,
num=2
num*=3
print(num)
#6

##to operate on numbers we have two build in functions in python
#abs, round functions
#abs, if we give input as negative number, it will give positive number as OUTPUT
#round --it will round of to nearest integer value
print(abs(-3))
#3

#round the first digit
print(round(3.75))
#4

#round the digit after first decimal point
print(round(3.75,1))
#3.8

##now its time for the comparison operations
#greate than            3>2
#less than              3<2
#equal                  3==2
#not equal              3!=2
#greate than or equal   3>=2
#less than or equal     3<=2
num_1=3
num_2=2
print(num_1==num_2)
#single equal is for assignment, double equal is for the comparison operation
#output is False
print(num_1!=num_2)
#output is True

print(num_1>num_2)
print(num_1<num_2)
print(num_1>=num_2)
print(num_1<=num_2)
#True
#False
#True
#False

##addition of strings won't do addition it just do concatination
num_1='100'
num_2='200'
print(num_1+num_2)
#output is 100200

##we need to do type casting then we need to add
num_1='100'
num_2='200'
num_1=int(num_1)
num_2=int(num_2)
print(num_1+num_2)
#output is 300
