##list sequence of data
##set unordered collection of data with no duplicates
courses=['maths','physics','chemistry']
print(courses)
#output is ['maths', 'physics', 'chemistry']

##length of list
print(len(courses))
#3

##list we can acess by using indexing and slicing
print(courses[0])
#maths
print(courses[2])
#chemistry
#print(courses[3])
#error list index out of range

#slicing with lists, first index is inclusive, second index is exclusive
print(courses[0:2])
print(courses[:2])
print(courses[1:])
#['maths', 'physics']
#['maths', 'physics']
#['physics', 'chemistry']

##operations with list methods, append, insert
#append with add at the end
courses.append('art')
print(courses)
#['maths', 'physics', 'chemistry', 'art']

##insert function takes two arguments, fisrt one is index where we want to insert
courses.insert(0,'art')
print(courses)
#['art', 'maths', 'physics', 'chemistry', 'art']

##insert function takes two arguments, fisrt one is index where we want to insert
## we can have list inside the list
courses1=['arts','science']
courses.insert(0,courses1)
print(courses)
#[['arts', 'science'], 'art', 'maths', 'physics', 'chemistry', 'art']
print(courses[0])
#output is ['arts', 'science']

##if we need use append or insert it is going as list inside the list, it is not merging with the list
courses=['maths','physics','chemistry']
courses.append(courses1)
print(courses)
#['maths', 'physics', 'chemistry', ['arts', 'science']]
##
courses=['maths','physics','chemistry']
courses.extend(courses1)
print(courses)
#['maths', 'physics', 'chemistry', 'arts', 'science']

##remove function removes inplace
courses=['comsci','maths','physics','chemistry']
courses.remove('maths')
print(courses)
#['comsci', 'physics', 'chemistry']

##pop function removes last elemnt like a stack
##also pop function while removed it returns or stores value in some variable
courses=['comsci','maths','physics','chemistry']
pop_removed=courses.pop()
print(pop_removed)
print(courses)
#chemistry
#['comsci', 'maths', 'physics']


#reverse the list based on alphabetical order
courses=['maths','physics','chemistry']
courses.reverse()
print(courses)
#['science', 'arts', 'chemistry', 'physics', 'maths']

#sort the list based on alphabetical order
courses.sort()
print(courses)
#['arts', 'chemistry', 'maths', 'physics', 'science']

#numbers inside the lists
courses=['maths','physics','chemistry']
num=[1,2,5,7]
courses.sort()
num.sort()
print(courses)
print(num)
#['chemistry', 'maths', 'physics']
#[1, 2, 5, 7]

##to get the sorted list in the decending order
courses=['maths','physics','chemistry']
num=[1,2,5,7]
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)
#['physics', 'maths', 'chemistry']
#[7, 5, 2, 1]

#sort methoed to sorting inplace, to avoid sorting in place we have sorted method
courses=['maths','physics','chemistry']
sorted(courses)
print(courses)
#nothing is updated here, because sorted function does not updte inplace['maths', 'physics', 'chemistry']
sorted_courses=sorted(courses)
print(sorted_courses)
#['chemistry', 'maths', 'physics']

#we have min,max,sum functions with the lists
num=[1,2,5,7]
print(min(num))
print(max(num))
print(sum(num))
#1
#7
#15

#we can get the index value of value in a lists
courses=['maths','physics','chemistry']
print(courses.index('chemistry'))
#output is 2

#we can get the index value of value in a lists
courses=['maths','physics','chemistry']
#print(courses.index('art'))
#we will get error because this index is not in the range
print('chemistry' in courses)
#True

##getting value in string using the in function, useful in for loops
for item in courses:
    print(item)
#output is same as below
#maths
#physics
#chemistry

##getting value and index in string using the enumarate function
for index,course in enumerate(courses):
    print(index,course)
#0 maths
#1 physics
#2 chemistry

##getting value and index in string using the enumarate function
for index,course in enumerate(courses,start=1):
    print(index,course)
#1 maths
#2 physics
#3 chemistry

##join method
courses=['maths','physics','chemistry']
course_str=','.join(courses)
print(course_str)
#output is maths,physics,chemistry
courses=['maths','physics','chemistry']
course_str='-'.join(courses)
print(course_str)
#output is maths-physics-chemistry

##we can put again back from string verson to the list version using split method
new_str=course_str.split('-')
print(new_str)
#output is ['maths', 'physics', 'chemistry']

########tuples
##only difference between the list and tuple are list is mutable, whereas tuple is immutable
list1=['math','phy','che','eng']
list2=list1
print(list1)
print(list2)
#output is ['math', 'phy', 'che', 'eng']
#output is ['math', 'phy', 'che', 'eng']
list1[0]='art'
print(list1)
print(list2)
#['art', 'phy', 'che', 'eng']
#['art', 'phy', 'che', 'eng']

##tuples
tuple1=('math','phy','che','eng')
tuple2=tuple1
print(tuple1)
print(tuple2)
#output is ('math', 'phy', 'che', 'eng')
#output is ('math', 'phy', 'che', 'eng')
#tuple1[0]='art'
#error 'tuple' object does not support item assignment


##lists are mutable, tuples are immutable
##remove, replace, append..these kind of methods won't work for tuples
#remaining things like loop through all are same as like lists


#sets
##sets are unordered also no duplicates
course_set={'math','phy','che','eng'}
print(course_set)
print(course_set)
#{'phy', 'che', 'eng', 'math'}
#{'phy', 'che', 'eng', 'math'}
course_set={'math','phy','che','eng','math'}
print(course_set)
#{'phy', 'che', 'eng', 'math'}

print('math' in course_set)
#True

#intersection, difference,union operations with strings
course_set={'his','math','phy','che'}
arts_set={'his','math','art','des'}
print(course_set.intersection(arts_set))
print(course_set.difference(arts_set))
print(course_set.union(arts_set))
#{'math', 'his'}
#{'che', 'phy'}##these are only in corse set, not there inarts set
#{'his', 'des', 'phy', 'art', 'math', 'che'}


##how to create empty lists, tuples and sets
#empty_list
empty_list=[]
empty_list=list()

#empty_tuple
empty_tuple=()
empty_tuple=tuple()

#empty_set
empty_set={}#wrong, it means empty dictionary
empty_list=set()
