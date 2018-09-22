nums=[1,2,3,4,5]
for num in nums:
    print(num)
#output is
#1
#2
#3
#4
#5

# we have break and continue statements with loops
#when condtion is true, break statement never allow to executes remaining iterations of the loops
#it will terminate the loop excution further
nums=[1,2,3,4,5]
for num in nums:
    if num==3:
        print('Found!')
        break
    print(num)
#output is
#1
#2
#Found!

##continue statement
#will skip next statements in the loop for the current iteration,
#example in this case when number is 3, it will skip the print(num) statement for the num=3,
#when num is not three, it will continue the loop as usual
nums=[1,2,3,4,5]
for num in nums:
    if num==3:
        print('Found!')
        continue
    print(num)
#output is
#1
#2
#Found!
#4
#5

#nested loops
for num in nums:
    for letter in "abc":
        print(num,letter)
#output is
#1 a
#1 b
#1 c
#2 a
#2 b
#2 c
#3 a
#3 b
#3 c
#4 a
#4 b
#4 c
#5 a
#5 b
#5 c

##we can use range function with the loops, instead of giving all numbers
#starts from zero default, not includes last character
nums=range(10)
for num in nums:
    print(num)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

#for the range function we can give from where to start
nums=range(1,11)
for num in nums:
    print(num)
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

##while loop,
##for loop iterates through all elements in the list
#while loop executes only when condition is True
#if we don't give x+=1, then while loop never ends, it will become infinite loop
x=0
while x<10:
    print(x)
    x+=1
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

#break statement working is same in while  loop also
x=0
while x<10:
    if x==5:
        print('Found')
        break
    print(x)
    x+=1
#1
#2
#3
#4
#Found

#insted of giving condtion after while, we can give condition like below also
x=0
while True:
    if x==5:
        print('Found')
        break
    print(x)
    x+=1
#1
#2
#3
#4
#Found

#if we don't give x+=1 statement , then while loop goes to infinite execution
#to terminate that we have to use control+c
x=0
while True:
    if x==5:
        print('Found')
        break
    print(x)

#0
#0
#0
#0
#0
#0
#.
#.
#.
