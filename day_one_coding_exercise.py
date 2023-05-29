# Exercice 1 - Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Exercise 2 - Debugging Practice
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Exercise 3 - Input Function
name = input("What is your name? ")
print(len(name))
print(len(input("What is your name? ")))

name = input("What is your name?")
length = len(name)
print(length)

# Exercise 4 - Variables
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

# Band Name Generator
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city + pet
#5. Make sure the input cursor shows on a new line:
print("Your band name could be ", band_name)
print("Your band name could be ", city + " " + pet)
print("Your band name could be " + city + " " + pet)
# Solution: https://replit.com/@appbrewery/band-name-generator-end