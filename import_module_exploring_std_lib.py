#we can import directory only currect file and impoertd files in the same directory
import input_import_module_exploring_std
courses=['mat','cat','rat']
print(input_import_module_exploring_std.find_index(courses,'rat'))
#calling find_index function from the imported module

#when we import the module we can use all variables and functions from that module
#when we import module if print stagements are there outside directly executes the statements
#output is
#imported my module
#1


##insted of using input_import_module_exploring_std this module every where we can rename that module name to our
#convinient name
import input_import_module_exploring_std as me
courses=['mat','cat','rat']
print(me.find_index(courses,'rat'))
#calling find_index function from the imported module, with the module name as me
#output is same as above
#imported my module
#1




##insted of using the module name while calling the fuctions from the imported module
#if we import the function from that module
#convinient name
from input_import_module_exploring_std import  find_index
##one thing  to remember is that it only gives access to that variable, not everything else
courses=['mat','cat','rat']
print(find_index(courses,'rat'))
#here we can directly use the find_index , without using module name
#output is same as above
#imported my module
#1


#if we want to use test variable from the imported function import like this
##below import gives only access to find_index, test from the imported module
from input_import_module_exploring_std import  find_index,test
courses=['mat','cat','rat']
print(find_index(courses,'rat'))
print(test)
##this print statement from the imported module executed only once  print('impoerted my module')
##output is
#1
#Test string

#we can rename find_index function in the present module as like below
#but this does not look good if some new programmers are looking at our code
from input_import_module_exploring_std import  find_index as ff,test
courses=['mat','cat','rat']
print(ff(courses,'rat'))
print(test)
#1
#Test string

##if we import specic functions or variables from the module, then we have access to only those
#not have access to all
#to import everything from the module use asterisk, drawback with this is in the 100's of lines of code
#we don't know from which module find_index function came, it is not good practice to use in this way
from input_import_module_exploring_std import  *
courses=['mat','cat','rat']
print(find_index(courses,'rat'))
print(test)
#output is same as above

##when we import module where all it checks
#it checks in the current directory and the file system(where python standard library sits)
## to see those paths , import sys module
import sys
print(sys.path)
#output is ['C:\\Users\\hamsals\\Desktop\\pythonlearning', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages']
#in this output first path is the directory from where we are running the script , remaing paths are python path environmetal variables
#rest all are python packages paths where python is installed


##importing module from the another directory, which is not current working directory
#import module_in_diff_location
#output the above line is below error
#ModuleNotFoundError: No module named 'module_in_diff_location'

#for not to get the error when we import the module from different location(not current working directory)
#we need to append this path to sys.path list
#sys.path is a list data type,
#where all the paths are present(when we are importing some module , that module should be present in this list)
import sys
sys.path.append('c:\\Users\\hamsals\\Desktop\\samsung')
print(sys.path)
#see now in the output list we got that module directort
#['C:\\Users\\hamsals\\Desktop\\pythonlearning', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\python37.zip', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\DLLs', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\lib', 'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32',
#'C:\\Users\\hamsals\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages', '/c/Users/hamsals/Desktop/samsung']
#here that module is in the samsung directory

#after appending that module directory, now it will import successfully
import module_in_diff_location
#output is as below
#impo module from the another directory, which is not current working directory
#importd from the another directory successfully


##appedning many paths at different location to sys.path, we got confused at the end
#because same module we can keep in multiple locations
# so always good programmers will add the new module to PYTHONPATH environmetal variable, which is the unique standard library place
#settings will be different in mac and windows
#in the office laptop these settings are not present


##now lets look at the usage of some of the standard functions from the python llibrary
import random
courses=['maths','phy','che']
random_value=random.choice(courses)
print(random_value)
#output is every time when we run the code we get different output
#after first run output is che
#after first run output is maths
#after first run output is phy


##here he is not going to cover all the standard library functions
#lets brifely look into the some of the useful functions
#to convert degrees to radians
import math
rad=math.radians(90)
print(rad)
#to get the sin of the radians
print(math.sin(rad))
#output is 1.5707963267948966
#1.0

import datetime
import calendar
today=datetime.date.today()
print(today)
#output is today's date 2018-09-22

print(calendar.isleap(2017))
#output is False

print(calendar.isleap(2020))
#output is True

#below we are using os to get the current workin directory
#os is a file system, it will scan entire file system and with the we can create files and delete files
import os
print(os.getcwd())
#output for the above print statement is C:\Users\hamsals\Desktop\pythonlearning


#below statementgives the location of the file
print(os.__file__)
#the above print statement print the  C:\Users\hamsals\AppData\Local\Programs\Python\Python37-32\lib\os.py
# if i do this we will get the code of this file cat ../../AppData/Local/Programs/Python/Python37-32/lib/os.py


##someother standard library files, in this module we have web browser open
#import antigravity
#output is web browser will open

#cat ../../AppData/Local/Programs/Python/Python37-32/lib/antigravity.py
#import webbrowser
#import hashlib
#webbrowser.open("https://xkcd.com/353/")
#def geohash(latitude, longitude, datedow):
    '''Compute geohash() using the Munroe algorithm.

    >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543

    '''
#    # http://xkcd.com/426/
#    h = hashlib.md5(datedow).hexdigest()
#    p, q = [('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
#    print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))
