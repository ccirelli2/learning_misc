#Research Hexadecimal, octal, and binary literals

#Example of a hexadecimal
a = 3
print(hex(a))

##Python includes built in numeric operators
#+, -, *, **, &, etc

##Built in mathematical functions
#pow, abs, round, int, hex, bin, etc.

##Python Expression Operator
#most fundamental tool to process numbers, 

#Example of an if/then/else statement.
x = 1
y = 2
z = 3

if y > 2:
	print(x) 
else: 
	print(z) 

#Example x in y then 
D = {}
D['cars']=  ['dodge', 'chrysller', 'ford']
D['colors']= ['red','blue','green']
print(D)

if 'dodge' in D['cars']:
	print(D['cars'])
else:
	print(D['colors'])
	
#Number operations

a = 3
a%2
print(a%2)

#Division: Classic, Floor, and True
#Two types of division in Python. / and //

/ # Natural division.  Will give you the results expected for a float with decimals
// #Called Floor division.  This operator always truncates fractional remainders. 
#Examples

d = 1.2
e = 4.3
f = 1.00008

ex = 4.3/1.2 #if you were to change the / to // the output would be truncated to 3.0. 
print(ex)

#Functions
#Float: will allow a float number to stay a float despite the operator (/ or //)
#NOTE:  Import math in order to be able to use the floor and trunc functions. 


import math
math.trunc(2.5)
print(math.trunc(2.5))

print(math.floor(2.5))













