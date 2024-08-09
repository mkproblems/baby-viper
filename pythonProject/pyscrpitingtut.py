# print("Hello World")

## String concatitnation
# print("Hello" + " " + "World")

## Input Variable
# name = input("What is your name? ")

## f string
# print(f"Hello {name}")

## Drawing out info in string, basic
# name = "Tommy"
# print(name[2])

#--------------------------------------------------
### Challenge 1 ###

# 1. create an input with a greeting

# 2. Ask What is their favorite food

# 3 Ask What is their favorite hobby

# 4. print with an f string their favorite food and hobby

# print("Hey!")
# name = input("What is your name? ")
# print(f"Hello {name}")
# food = input("What is your favorite food? ")
# print(f"{food} is delicious!")
# hobby = input("What do you do for fun? ")
# print("I like that too!")
# print(f"{food}" + " and " + f"doing {hobby}, you're quite interesting!")

#-----------------------------------------------------

### Recap ###

# string = "my string"

# float = 3.14

# boolean = true / false

### Why types matter ###

# var = float(123)
# print(type(var))

# var = str(123)
# print(type(var))

### You cannot concatonate a str and a var
# var = ("123")
# var2 = 3
# var3 = var + var2

# print(78 + int("70"))

# print("70" + "70")

#-----------------------------------------------------
### Challenge 2 ###

# num1 = "12345"
# num2 = "67898"
# num3 = "87654"

# Add num1 and num2

# Add the second number in num1 and the second number in num3

# Change num2 into a float and print the type to the console as a float

# print(num1 + num2)
# print(int(num1) + int(num2))

# print("-----------------------------")

# print(num1[1] + num3[1])
# print(int(num1[1]) + int(num3[1]))

# print("-----------------------------")

# print(type(float(num2)))

#-----------------------------------------------------

### If / Elif input ###

# If you are under 5 you are a kid
# If you are 5-15 you are a big kid
# if you are 15-21 you are a bigger kid
# If you are over 21 you are the biggest kid

# var = int(input("What is your age? "))

# if var <= 5:
#     print(f"WOW, {var}? You are a kid!")
# elif var <= 15:
#     print(f"WOW, {var}? You're a BIG kid!")
# elif var > 21:
#     print(f"{var}? You are a BIGGER kid!")

#-----------------------------------------------------

### Challenge 3 ###

# ask the usr for the temperature input
# if its less than 20 degrees you need boots
# if its less than 30 degrees you need a coat
# if its less than 70 you need a jacket
# if its over 70 it is nice outside


# var = int(input("What is the Temperature outside? "))

# if var <= 20:
#     print("You're gonna need Boots!")
# elif var <= 30:
#     print("Don't forget your Coat!")
# elif var <= 70:
#     print("Sounds like Jacket weather!")
# elif var > 70:
#     print("That's perfect!")
## Could also do else

#-----------------------------------------------------

### For Loops ###

## Basic For loop
# string = "hello world"
# for i in string:
#     print(i)
# print(string)

### Lists ###

## This prints every item in the list in order, and then prints just the 2nd item in the list
# my_list = ["item1", "item2", "item3"]
# for i in my_list:
#     print(i)
# print(my_list[1])


### While loops ###
## This continue running a while loop by increasing i by 1, and exits the loop when a str of "n" is entered

# on = True
# i = 0
# while on:
#     var = input("Continue running while loop y or n? ")
#     i += 1
#     print(i)
#     if var == "n":
#         on = False


### Functions ###

# def my_function(i):
#     var = int(i) + 3
#     print(var)
#
# my_function(input(" what would you like to add? "))

### Challenge 4 ###

## Input first letter of your name
## calla  fnction that adds the first letter to the rest of yourt name
# def add_name():
#     var = input("? ")
#     if var == "n" or var == "N":
#         print(str(var) + "ate")
#     else: (print("Wrong!"))
# add_name()

#-----------------------------------------------------

### Building a Recon Tool ###

## automating Recon
# def nmap(ip):
#     var = f"nmap -A - p - {ip} - v"
#     print(f"Running nmap scan against {var}")
#
# nmap(input("What IP would you like to scan? "))


