#!/bin/python3

# Print String

print("strings and things:")
print('hello, world')
print("""hello, this is
a multi
line string""")
print("This is"+"A string")
print('\n') #New Line

#Python Math

print("Math time:")
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #Multiply
print(50 / 50) #divide
print(50 ** 2) #exponents
print(50 % 6) #modulo, divide but give remainder
print(50 // 6) #divide, but give only integer 
print('\n')

#variables and methods

print('fun with variables and methods:')
quote = 'all be fair, maties'
print(len(quote)) #prints the length of the variable <quote>
print(quote.upper()) #makes quote all uppercase
print(quote.lower()) #prints as all lowercase
print(quote.title()) #prints in titlecase
print('\n')

name = 'aurora'
age = 20 #intiger, can be delared also using int(29)
gpa =3.7 #float variable because of the . , float(3.7)
print(int(age))
print(int(29.9)) #using the int method removes anything past the decimal point
print('my name is ' + name + ' and I am ' + str(age) + ' years old') #name doesn't need to be converted to a string, because it already is one, but you can't add an intiger to strings without converting it using str()
print('\n')
age += 1 # += means add whatever follows to the given variable, and updates the variable to match, so age here is now equal to 21
print(age)
print('\n')

#functions

print('Function fun, ction....')

#functions define an area of code that can be later called back to, so if you used a piece of code many times, it'd be easier to make it a function, and then call back that function later
print('\n')
def who_am_i():
	name = "Aurora" #if name1 is not declared outside the function, it returns a null value 
	age = 20
	print('my name is ' + name + ' and I am ' + str(age) + ' years old')

who_am_i() #runs the block of code under who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#multiple parameters
def add(x, y):
	print(x + y)
add(123, 4321)

#using return
def multiply(x, y):
	return x * y
print(multiply(5,4)) #return makes the function act as though it had the value listed in the retun statement

def square_root(x):
	return x ** .5
print(square_root(16)) #retuns float, because .5 is a float

def newline():
	print('\n')

newline()
#Boolean Expressions, True/False

print('boolean expressions:')
bool1 = True
bool2 = 3*3 == 9 # the == is used for expressions, or evaluations, do not use = for evaluations
bool3 = False
bool4 = 3*3 != 9 # =! means does not equal
print(bool1,bool2,bool3,bool4)
print(type(bool1)) #checks type of variable
bool5 = 'True'
print(type(bool5)) #the '' around the True makes it a String, not a Bool variable

#relational boolean operators, logical operands

newline()
greater_than = 7 > 5
less_than = 5 > 7
greaterthan_equalto = 7 >= 7
lessthan_equalto = 7 <= 7

print(greater_than,less_than,greaterthan_equalto,lessthan_equalto)

test_and = (7 > 5) and (8 < 7) #one false statement makes the whole thing false
test_or = (7 > 5) or (8 < 7) #one true is still considered a true statement
test_not = not True #not reverses the answer
newline() 
print(test_and)

#conditional statements
print('Conditional Statements:')
newline()

def soda(money):
	if money >= 2:
		return "You got youself a soda pop"
	else:
		return "get lost broke boi lmao"
print(soda(3)) 
print(soda(1)) 

def alchohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting tipsy girls!"
	elif (age >= 21) and (money < 5):
		return "You broke lmao"
	elif (age < 21) and (money >= 5): #elif is else, if 
		return "Nice try bucko"
	else:
		return "too poor and too young lmao millenials"

print(alchohol(21,5))
print(alchohol(21,4))
print(alchohol(20,4))

newline()

#Lists
print("Lists have brackets []:")
movies = ["when harry met sally", "The Hangover", "The perks of being a wallflower", "The Exorcist"]

print(movies[0]) #prints the first item on the list, because they start counting lists at 0!!! don't forget is important
print(movies[0:2]) #pulls the first 2 items on the list, when making a call for multiple items in a list, you gotta go one over the one you actually want, think about it like all items from 0, up to but not including 2
print(movies[1:]) #called slicing, this starts at 1, then goes to all 
print(movies[:1]) #starts at 0, then ends at 1
print(movies[-1]) #-1 pulls the last item from the list
print(len(movies)) #prints number of items in list

movies.append("JAWS") #adds JAWS to the end of the list
print(movies)

movies.pop() # .pop removes an item from a list, by default the last one
print(movies)
newline()

movies.pop(1) #removes 'The Hangover' because it is the 2nd item on the list
print(movies)

movies = ["when harry met sally", "The Hangover", "The perks of being a wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Andromeda"]
combined = zip(movies,person) #zip stores it in memort somewhere? and combines the lists, if lists are different lengths, new list is the shortest length
print(list(combined))

#Tuples
print("Tuples have Parenthesis and cannot change, are immutable:")
#A Tuple is a list that cannot be modified
newline()
grades = ("A", "B", "C", "D", "F")
print(grades[1]) #tuples are unappendable and unpoppable

#Looping
print("For loops - start to finish of iterate:")
newline()
#for loops
veggies = ["cucumber", "spinach", "cabbage"]

for x in veggies:
	print(x) #x is an arbitrary variable, that takes the value of each item in the list for each loop

print("While loops - execute as long as True:")
i = 1
while i <= 10:
	print(i)
	i += 1 #adds 1 to i each loop, and runs as long as i is less than or equal to 10



