"""1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
"""
print("""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are""")

import sysconfig
"""2. Write a Python program to get the Python version you are using. Go to the editor
Click me to see the sample solution"""
print(sysconfig._PY_VERSION)

"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
Click me to see the sample solution
"""
import datetime

print(datetime.datetime.now())
"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
Click me to see the sample solution

import math
r=input("please enter the radius in:")
#print(type(r), math.pi)

print("Area in the same units: {}".format((math.pi)*(float(r)**2)))


5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor
Click me to see the sample solution

name=input("Please enter your name (first last):")
name.strip()
names=name.split()
print(names[1]+" "+names[0])


6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
Click me to see the sample solution

neww=input("enter sample data with comma seperators: ")
neww=neww.replace(" ","")
lists=neww.split(",")
print(len(lists))
tuples=tuple(lists)
print(tuples)
print("List: {} \n Tuples:{}".format(lists,tuples))

7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
Click me to see the sample solution

file_name=input("please enter the file name with extension:")
print(file_name[file_name.find(".")+1:])

8. Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
Click me to see the sample solution
"""
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1] )
"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
Click me to see the sample solution
"""
exam_st_date = (11, 12, 2014)
print("The examinations start from: {} / {} / {}".format(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
Click me to see the sample solution
"""
number= 5 #input("please input the number:")
print(int(number)+int(number*2)+int(number*3))

"""

11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
Click me to see the sample solution

?????????????????????????????????/
function_name= 'abs'
function_name.rstrip("()")
print(abs.__doc__)
????????????????????????????????????


12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
Click me to see the sample solution
"""
import calendar
print(calendar.month(2019,5))
"""
13. Write a Python program to print the following here document. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
Click me to see the sample solution

14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
Click me to see the sample solution
"""
Sample_dates= ((2014, 7, 2), (2014, 7, 11))
from datetime import date as tds
x,y,z=Sample_dates[0]
t1=tds(x,y,z)
print(t1)
x,y,z=Sample_dates[1]
t2=tds(x,y,z)
t3=t2-t1
print(abs(t3))

"""
15. Write a Python program to get the volume of a sphere with radius 6.
Click me to see the sample solution
"""
import math
r=6
print("area of sphere:{} when radius is 6 ".format((4/3)*math.pi*(r**3)))
"""

16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. Go to the editor
Click me to see the sample solution
"""
number = 5#int(input("Please provide a number:"))
diff= number-17
if diff<0:
    print(abs(diff))
else:
    print(diff*2)
"""

17. Write a Python program to test whether a number is within 100 of 1000 or 2000. Go to the editor
Click me to see the sample solution

number = int(input("Please provide a number:"))
if (abs(1000-number)<100 or abs(2000-number)<100):
    print(True)
else: 
    print(False)

18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum. Go to the editor
Click me to see the sample solution
"""
def three_numbers(a,b,c):
    if (a==b and a==c):
        return 9*a
    else:
        return a+b+c

print(three_numbers(1,2,3))

print(three_numbers(2,2,2))
"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor
Click me to see the sample solution

string=input("Please enter as string:")
if string[:2] == "Is":
    print(string)
else:
    print("Is"+string)

20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. Go to the editor
Click me to see the sample solution
"""
number= 2#int(input("Please input the number of time you need the 'sam' repetition:"))
if number<0:
    print('sam'*abs(number))
else:
    print("sam"*number)
"""
21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. Go to the editor
Click me to see the sample solution
"""
number= 2#int(input("please provide a number:"))
if number%2==0:
    print("given number is even")
else:
    print("number is odd")
"""
22. Write a Python program to count the number 4 in a given list. Go to the editor
Click me to see the sample solution
"""
lists=[1,3,4,3,5,4,6]
print(lists.count(4))

"""

23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. Go to the editor
Click me to see the sample solution

number= int(input("Please input the number "))
string= input("Please input the string")
print(string[:2]*number)

24. Write a Python program to test whether a passed letter is a vowel or not. Go to the editor
Click me to see the sample solution

vowel=['a','e','i','o','u']
letter=str(input("Please enter the letter:")).lower()
if letter in vowel:
    print("the letter is a vowel")
else:
    print("not a vowel")

25. Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

number = int(input("please input a number:"))
print(number in C)

Click me to see the sample solution

26. Write a Python program to create a histogram from a given list of integers. Go to the editor
Click me to see the sample solution
"""
lists=[1, 5, 8, 3]
for i in lists:
    print('-'*i)

"""
27. Write a Python program to concatenate all elements in a list into a string and return it. Go to the editor
Click me to see the sample solution
"""
lists=[1,5.1,2+5j,"sam"]
string=''
for i in lists:
    print(i)
    string+=str(i)
print(string)
"""
28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :
"""
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for i in numbers:
    if i%2==0:
        print(i)
    if i ==237:
        break
"""
Click me to see the sample solution

29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
Test Data :
"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

"""Expected Output :
{'Black', 'White'}
Click me to see the sample solution

30. Write a Python program that will accept the base and height of a triangle and compute the area. Go to the editor
Click me to see the sample solution

base=float(input("Please provide base:"))
height=float(input("Please provide height:"))
print("Area = {}".format((1/2)*height*base))

31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. Go to the editor
Click me to see the sample solution

n1=int(input("Please provide n1:"))
n2=int(input("Please provide n2:"))

print(math.gcd(n1,n2))

32. Write a Python program to get the least common multiple (LCM) of two positive integers. Go to the editor
Click me to see the sample solution

n1=int(input("Please provide n1:"))
n2=int(input("Please provide n2:"))

LCM=(abs(n1*n2)//math.gcd(n1,n2))
print(LCM)

33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. Go to the editor
Click me to see the sample solution
"""
a,b,c=1,2,4
if (a==b or b==c or c==a):
    print("sum= 0")
else: 
    print(a+b+c)
"""
34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor
Click me to see the sample solution

"""
a,b=6,5
if (a+b>15 and a+b<20 ):
    print(20)
else:
    print(a+b)
"""

35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. Go to the editor
Click me to see the sample solution
"""
x,y=4,5
#print((x==y or (abs(x+y)==5 or abs(x-y)==5)))

"""

36. Write a Python program to add two objects if both objects are an integer type. Go to the editor
Click me to see the sample solution

"""
x=2
y=3
sum
if type(x)==int and type(y)==int: 
    sum= x+y 
else:
    sum=False
print(sum)

""""
37. Write a Python program to display your details like name, age, address in three different lines. Go to the editor
Click me to see the sample solution
"""
for i in {"name":"sam","age":27,"address":"none of your"}.items():
    print(i[0]+":"+str(i[1]))

"""

38. Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
Click me to see the sample solution
"""
x = 4
y = 3
print((x+y)**2)
"""

39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the editor
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
Click me to see the sample solution
"""
amt = 10000
rate = 3.5
years = 7
future_value=amt
for i in range(years):
   future_value+=(future_value*rate)/100
   # print(i,future_value)
print(future_value)

"""
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). Go to the editor
Click me to see the sample solution

"""
z1=(3,4)
z2=(4,5)

print(math.sqrt((z1[0]-z2[0])**2 + (z1[1]-z2[1])**2))
"""

41. Write a Python program to check whether a file exists. Go to the editor
Click me to see the sample solution
"""
import os.path
print(os.path.lexists("../Python150.py"))
"""

42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. Go to the editor
Click me to see the sample solution
"""
import sys

if (sys.maxsize>2**32):
    print("64bit")
else:
    print("32bit")

"""
43. Write a Python program to get OS name, platform and release information. Go to the editor
Click me to see the sample solution
"""
import os
import platform
print(os.name)
print(platform.system())
print(platform.release())
"""
44. Write a Python program to locate Python site-packages. Go to the editor
Click me to see the sample solution

45. Write a python program to call an external command in Python. Go to the editor
Click me to see the sample solution

46. Write a python program to get the path and name of the file that is currently executing. Go to the editor
Click me to see the sample solution
"""
print(os.path.realpath(__file__))
"""
47. Write a Python program to find out the number of Cprint(sam)PUs using. Go to the editor
Click me to see the sample solution

48. Write a Python program to parse a string to Float or Integer. Go to the editor
Click me to see the sample solution

49. Write a Python program to list all files in a directory in Python. Go to the editor
Click me to see the sample solution
"""

"""

50. Write a Python program to print without newline or space. Go to the editor
Click me to see the sample solution

51. Write a Python program to determine profiling of Python programs. Go to the editor
Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
Click me to see the sample solution

52. Write a Python program to print to stderr. Go to the editor
Click me to see the sample solution

53. Write a python program to access environment variables. Go to the editor
Click me to see the sample solution

54. Write a Python program to get the current username Go to the editor
Click me to see the sample solution

55. Write a Python to find local IP addresses using Python's stdlib Go to the editor
Click me to see the sample solution

56. Write a Python program to get height and width of the console window. Go to the editor
Click me to see the sample solution

57. Write a program to get execution time for a Python method. Go to the editor
Click me to see the sample solution
"""
import time 
start=time.time()
for i in range(5): print("just checking")
end=time.time()
print(end-start)
"""
58. Write a python program to sum of the first n positive integers. Go to the editor
Click me to see the sample solution
"""
def sum_of_n (n:int):
    return (n* (n-1))/2

start=time.time()
print(sum_of_n(20))
end=time.time()
print(start-end)
"""

59. Write a Python program to convert height (in feet and inches) to centimeters. Go to the editor
Click me to see the sample solution

height=input("Please provide height in \'\" format:")
height.strip()
feet=float(height[:height.find("'")])
inches=float(height[height.find("'")+1:height.find('"')])
height_cm=((feet*12)+inches)*2.54
print(height_cm)

60. Write a Python program to calculate the hypotenuse of a right angled triangle. Go to the editor
Click me to see the sample solution
"""
base =3
height=4
hypotenuse=math.sqrt(base**2 + height**2)
print(hypotenuse)
"""
61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. Go to the editor
Click me to see the sample solution
"""
feet=40
mile=feet/5280
yard=feet/3
inches=feet*12
print(mile,yard,inches)

"""
62. Write a Python program to convert all units of time into seconds. Go to the editor
Click me to see the sample solution

63. Write a Python program to get an absolute file path. Go to the editor
Click me to see the sample solution

64. Write a Python program to get file creation and modification date/times. Go to the editor
Click me to see the sample solution

65. Write a Python program to convert seconds to day, hour, minutes and seconds. Go to the editor
Click me to see the sample solution
min=sec/60
hour=sec/3600
day=sec/43200 
66. Write a Python program to calculate body mass index. Go to the editor
Click me to see the sample solution
BMI = weight in kg / heigh in mts **2 

67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. Go to the editor
Click me to see the sample solution

68. Write a Python program to calculate the sum of the digits in an integer. Go to the editor
Click me to see the sample solution

integer= input("digit please :")
sum=0
for i in integer:
    sum+=int(i)
print(sum)


69. Write a Python program to sort three integers without using conditional statements and loops. Go to the editor
Click me to see the sample solution
use min max

70. Write a Python program to sort files by date. Go to the editor
Click me to see the sample solution


71. Write a Python program to get a directory listing, sorted by creation date. Go to the editor
Click me to see the sample solution

72. Write a Python program to get the details of math module. Go to the editor
Click me to see the sample solution


73. Write a Python program to calculate midpoints of a line. Go to the editor
Click me to see the sample solution
x1+x2/2
y1+y2/2

74. Write a Python program to hash a word. Go to the editor
Click me to see the sample solution

hash(word)

75. Write a Python program to get the copyright information. Go to the editor
Click me to see the sample solution
sys.copyright

76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. Go to the editor
Click me to see the sample solution
"""
print(sys.argv)
"""
77. Write a Python program to test whether the system is a big-endian platform or little-endian platform. Go to the editor
Click me to see the sample solution

78. Write a Python program to find the available built-in modules. Go to the editor
Click me to see the sample solution

79. Write a Python program to get the size of an object in bytes. Go to the editor
Click me to see the sample solution

80. Write a Python program to get the current value of the recursion limit. Go to the editor
Click me to see the sample solution

81. Write a Python program to concatenate N strings. Go to the editor
Click me to see the sample solution
.join(iterable)

82. Write a Python program to calculate the sum over a container. Go to the editor
Click me to see the sample solution
sum(container)  builtin functions

83. Write a Python program to test whether all numbers of a list is greater than a certain number. Go to the editor
Click me to see the sample solution
all()
brute force 
sort reverse=true, first elemnt check

84. Write a Python program to count the number occurrence of a specific character in a string. Go to the editor
Click me to see the sample solution
st.count()
85. Write a Python program to check if a file path is a file or a directory. Go to the editor
Click me to see the sample solution
os.path.isfile()
.isdir()

86. Write a Python program to get the ASCII value of a character. Go to the editor
Click me to see the sample solution

87. Write a Python program to get the size of a file. Go to the editor
Click me to see the sample solution

88. Given variables x=30 and y=20, write a Python program to print t "30+20=50". Go to the editor
Click me to see the sample solution

89. Write a Python program to perform an action if a condition is true. Go to the editor
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
Click me to see the sample solution

90. Write a Python program to create a copy of its own source code. Go to the editor
Click me to see the sample solution

91. Write a Python program to swap two variables. Go to the editor
Click me to see the sample solution
c=a
a=b
b=c

92. Write a Python program to define a string containing special characters in various forms. Go to the editor
Click me to see the sample solution

93. Write a Python program to get the identity of an object. Go to the editor
Click me to see the sample solution

94. Write a Python program to convert a byte string to a list of integers. Go to the editor
Click me to see the sample solution

95. Write a Python program to check if a string is numeric. Go to the editor
Click me to see the sample solution

96. Write a Python program to print the current call stack. Go to the editor
Click me to see the sample solution

97. Write a Python program to list the special variables used within the language. Go to the editor
Click me to see the sample solution

98. Write a Python program to get the system time. Go to the editor

Note : The system time is important for debugging, network information, random number seeds, or something as simple as program performance.
Click me to see the sample solution

99. Write a Python program to clear the screen or terminal. Go to the editor
Click me to see the sample solution

100. Write a Python program to get the name of the host on which the routine is running. Go to the editor
Click me to see the sample solution

101. Write a Python program to access and print a URL's content to the console. Go to the editor
Click me to see the sample solution

102. Write a Python program to get system command output. Go to the editor
Click me to see the sample solution

103. Write a Python program to extract the filename from a given path. Go to the editor
Click me to see the sample solution

104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. Go to the editor
Note: Availability: Unix.
Click me to see the sample solution

105. Write a Python program to get the users environment. Go to the editor
Click me to see the sample solution

106. Write a Python program to divide a path on the extension separator. Go to the editor
Click me to see the sample solution

107. Write a Python program to retrieve file properties. Go to the editor
Click me to see the sample solution

108. Write a Python program to find path refers to a file or directory when you encounter a path name. Go to the editor
Click me to see the sample solution

109. Write a Python program to check if a number is positive, negative or zero. Go to the editor
Click me to see the sample solution
if x>0 (positive)
elif x<0 (negative)
else 0

110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. Go to the editor
Click me to see the sample solution
"""
a=[1,2,15,45,30,3,5]

"""

111. Write a Python program to make file lists from current directory using a wildcard. Go to the editor
Click me to see the sample solution

112. Write a Python program to remove the first item from a specified list. Go to the editor
Click me to see the sample solution

113. Write a Python program to input a number, if it is not a number generate an error message. Go to the editor
Click me to see the sample solution

114. Write a Python program to filter the positive numbers from a list. Go to the editor
Click me to see the sample solution

115. Write a Python program to compute the product of a list of integers (without using for loop). Go to the editor
Click me to see the sample solution

116. Write a Python program to print Unicode characters. Go to the editor
Click me to see the sample solution

117. Write a Python program to prove that two string variables of same value point same memory location. Go to the editor
Click me to see the sample solution

118. Write a Python program to create a bytearray from a list. Go to the editor
Click me to see the sample solution

119. Write a Python program to display a floating number in specified numbers. Go to the editor
Click me to see the sample solution

120. Write a Python program to format a specified string to limit the number of characters to 6. Go to the editor
Click me to see the sample solution

121. Write a Python program to determine if variable is defined or not. Go to the editor
Click me to see the sample solution

122. Write a Python program to empty a variable without destroying it. Go to the editor

Sample data: n=20
d = {"x":200}
Expected Output : 0
{}

Click me to see the sample solution

123. Write a Python program to determine the largest and smallest integers, longs, floats. Go to the editor
Click me to see the sample solution

124. Write a Python program to check if multiple variables have the same value. Go to the editor
Click me to see the sample solution

125. Write a Python program to sum of all counts in a collections? Go to the editor
Click me to see the sample solution

126. Write a Python program to get the actual module object for a given object. Go to the editor
Click me to see the sample solution

127. Write a Python program to check if an integer fits in 64 bits. Go to the editor
Click me to see the sample solution

128. Write a Python program to check if lowercase letters exist in a string. Go to the editor
Click me to see the sample solution

129. Write a Python program to add leading zeroes to a string. Go to the editor
Click me to see the sample solution

130. Write a Python program to use double quotes to display strings. Go to the editor
Click me to see the sample solution

131. Write a Python program to split a variable length string into variables. Go to the editor
Click me to see the sample solution

132. Write a Python program to list home directory without absolute path. Go to the editor
Click me to see the sample solution

133. Write a Python program to calculate the time runs (difference between start and current time) of a program. Go to the editor
Click me to see the sample solution

134. Write a Python program to input two integers in a single line. Go to the editor
Click me to see the sample solution

135. Write a Python program to print a variable without spaces between values. Go to the editor
Sample value : x =30
Expected output : Value of x is "30"
Click me to see the sample solution

136. Write a Python program to find files and skip directories of a given directory. Go to the editor
Click me to see the sample solution

137. Write a Python program to extract single key-value pair of a dictionary in variables. Go to the editor
Click me to see the sample solution

138. Write a Python program to convert true to 1 and false to 0. Go to the editor
Click me to see the sample solution

139. Write a Python program to valid a IP address. Go to the editor
Click me to see the sample solution

140. Write a Python program to convert an integer to binary keep leading zeros. Go to the editor
Sample data : 50
Expected output : 00001100, 0000001100
Click me to see the sample solution

141. Write a python program to convert decimal to hexadecimal. Go to the editor
Sample decimal number: 30, 4
Expected output: 1e, 04
Click me to see the sample solution

142. Write a Python program to find the operating system name, platform and platform release date. Go to the editor
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic
Click me to see the sample solution

143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system. Go to the editor
Click me to see the sample solution

144. Write a Python program to check if variable is of integer or string. Go to the editor
Click me to see the sample solution

145. Write a Python program to test if a variable is a list or tuple or a set. Go to the editor
Click me to see the sample solution

146. Write a Python program to find the location of Python module sources. Go to the editor
Operating system name:
posix
Platform name:
Linux
Platform release:
4.4.0-47-generic
Click me to see the sample solution

147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. Go to the editor
Click me to see the sample solution

148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. Go to the editor
Note: Do not use built-in functions.
Click me to see the sample solution

149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. Go to the editor
Click me to see the sample solution

150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values. Go to the editor
Click me to see the sample solution
"""