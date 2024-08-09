### Revisiting Print

# print('hello again')
# x = "Ryan"
# y = "John"
# print(f"{x} {y}")


# ip = input("What is the IP address? ")
# print("the IP you entered is " + ip)

# print("You are targeting " + input("What IP would you like to target? "))

### More about variables

# remember you can change types
# x = "5"
# y = 7
# print(int(x) + y)

## These variables take a first name and a last name
# first = input("First name? ")
# last = input("Last name? ")
# print(f" Your name is {first} {last}")
# print("Your name is " + first + " " + last)


## This takes input for pet name and a city and creates a twitter handle and bio
# print("Welcome to the program!")
# pet = input("What is your pet's name? ")
# city = input("Cute! what city were you born in? ")
# print(f"Your new Twitter handle will be.. @Cyber{pet} and the bio can be: from {city}")


# fnum = input("What is the first numba? ")
# snum = input("What is the second numba? ")
#
# if fnum > snum:
#     print("First num larger")
# elif snum > fnum:
#     print("Second num is larger")
# else:
#     print("the numbers are the same!")

# grade = input("What was your score? ")
# if int(grade) >= 90:
#     print("A")
# elif int(grade) >= 80:
#     print("B")
# elif int(grade) >= 70:
#     print("C")
# elif int(grade) >= 60:
#     print("D")
# else:
#     print("F")


## This shows the variable assigned by a list is just a representation of an item in the list, regardless of the variable used.
## Useful for when looping through data

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit + " pie")
#
# list = ["item1", "item2", "item3"]
#
# for item in list:
#     print(item)

## Find all numbers divisible by 2 from 1-100

# for num in range(0,100,2):
#     print(num)

# for num in range(0,100):
#     if num % 3 == 0:
#         print(num)


## Fizzbuzz
## if a number is divisible by 3, print fizz
## if a number is divisible by 5, print buzz
#if a number is divisble by both, print fizzbuzz

# for num in range(0,100):
#     if num % 3 == 0 and num % 5 == 0:
#         print("fizzbuzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)

### Functions

# import time
#
# choice = int(input("What number would you like to choose? "))
# def function(choice):
#     for num in range(0, choice):
#         if num % 3 == 0 and num % 5 == 0:
#             print("fizzbuzz")
#         elif num % 3 == 0:
#             print("fizz")
#         elif num % 5 == 0:
#             print("buzz")
#         else:
#             print(num)
#
# print("about to run the program")
# time.sleep(3)
# function(choice)


