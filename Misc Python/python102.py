#!/bin/python3

#Importing
print("Importing is important! c:")
#importing usually occours at the beginning of the script, but 
import sys #System Functions and Parameters

from datetime import datetime #imports a specific portion of a module
print(datetime.now()) #Prints whatever the current date/time is

from datetime import datetime as dt #Importing with an alias
print(dt.now()) #gives same results, can be used to rename calls

def newline():
	print('\n')

newline()

#advanced strings
print('advanced strings c:')
my_name = 'Andromeda'
print(my_name[0]) #Strings can be interpreted as a list of characters, and specific characters can be called as such
print(my_name[-1]) #calls the last character of a list or string
newline()
sentence = 'this is a sentence'

print(sentence[:4]) #prints the first 4 characters
print(sentence[-8:]) #prints the last 8 characters of the sentence
# -0 is the same as 0, that's maths babeyyyy
#Split method

print(sentence.split()) #Split sentence by delimiter (space by default)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) #uses the string at the beginning as a point between each item in the list sentence_split

print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)
#you can't say for example, "I said, "give me all the money"" on its own because of the matching quote marks

quoteception = "I said, \"give me all the money\""
print(quoteception) #the \ backslash makes the internal quotes valid

print("A" in "Apple") #returns True as a boolean argument
letter = 'a'
word = 'Apple'
print(letter in word) #case sensitive, will return false

print(letter.upper() in word.upper()) #by reading both strings as all upper or lowercase, the case is ignored, or always matching

word_two = 'Bingo'
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())) #not inverts the following result, this statement will return true

toomuchspace = '           hellp             '
print(toomuchspace.strip()) #strips out delimiter (space by default)
oopsname = 'ndromeda Weir' #editing strings
print(oopsname.replace('ndromeda', 'Andromeda')) 
print(oopsname.find('Weir')) #Prints the position in the string where the delimiter is found

movie = 'The Hangover'
print('My favorint movie is {}.'.format(movie)) #fills in {} with the given variable

def favbook(title, author):
	fav = 'my favorite book is \"{}\", which is written by {}'.format(title,author) #each placeholder is given in order
	return fav

print(favbook('The Great Gatsby','F. Scott Partyman'))


newline()
#dictionaries
print('Dirctionaries are keys and values:')
drinks = {'White russians': 7, "Old Fashioned": 10, "lemon Drop": 8, "Buttery Nipple": 6} #drink name is a Key, price is a Value

print(drinks)

employees = {'Finance': ['bob', 'linda', 'tina'], "IT": ['gene', 'louise', 'teddy'], "HR": ['Jimmy Jr.', 'mort']}
print(employees)

employees['legal'] = ['Mr. Frond'] #add a new key:value pair to the dictionary
print(employees)

employees.update({'Sales':['Andie', 'Ollie']})
print(employees)

drinks['White russians'] = 8 #updates the value associated with the key white russians
print(drinks)

print(drinks.get('White russians')) #returns value for given key
print(drinks.get('Martini')) #returns 'None'
print(drinks['White russians']) #returns value for key too

#list and dictionaries

movies = ["When harry met sally", "Perks of being a wallflower", "The Hangover", "The Exorcist"]
person = ["Andromeda", "Bob", "Leah", "Noelle"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}
print(movie_dictionary)
