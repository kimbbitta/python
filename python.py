#
#
# name = input("Hello! What's your name? ")
# age = input(f"Nice to meet you, {name}! What's your age? ")
# year = input("Thanks! Did you celebrate your birthday this year?")
#
# print (name)
# print(age)
# print (year)
#
# if year == 'yes':
#     if int(age) <= 0:
#         print ('Error. The number needs to be more than 0')
#     elif int(age) < 18:
#         birth_year = 2025 - int(age)
#             print (f"Thanks {name}, look's like you were born in {birth_year}, which means you're a minor.)
#     int(age) > 18:
#         birth_year = 2025 - int(age)
#             print(f"Thanks {name}, look's like you were born in {birth_year}, which means you're an adult.")


# name = input("Hello! What's your name? ")
# age = input(f"Nice to meet you, {name}! What's your age? ")
# year = input("Thanks! Did you celebrate your birthday this year? ")
#
# print (name)
# print(age)
# print (year)
#
# while True:
#     if year == 'yes':
#         if int(age) <= 0:
#            print ('Error. The number needs to be more than 0')
#         elif int(age) < 18:
#             birth_year = 2025 - int(age)
#             print (f"Thanks {name}, look's like you were born in {birth_year}, which means you're a minor.")
#         elif int(age) >= 18:
#             birth_year = 2025 - int(age)
#             print(f"Thanks {name}, look's like you were born in {birth_year}, which means you're an adult.")
#         elif int(age) > 110:
#             print("Number cannot exceed 110.")
#         else:
#             print('Please retry')
#
#     elif year == 'no':
#         if int(age) <= 0:
#             print ('Error. The number needs to be more than 0')
#         elif int(age) < 18:
#             birth_year = 2024 - int(age)
#             print (f"Thanks {name}, look's like you were born in {birth_year}, which means you're a minor.")
#         elif int(age) >= 18:
#             birth_year = 2024 - int(age)
#             print(f"Thanks {name}, look's like you were born in {birth_year}, which means you're an adult.")
#         elif int(age) > 110:
#             print("Number cannot exceed 110.")
#         else:
#             print('Please retry')


# total = 0
# for i in range(1,8):
#     if i % 3 == 0:
#         total += i
#         print (total)
#
# total = 0
# for i in range(1,100):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)

# total = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         total += i
# print(total)


# customer = {
#     "name: John Smith,"
#     "age: 30,

#DICTIONARIES
# answer = ""
# question = input("number: ")
# numbers = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
#
# for ch in question:
#     answer += numbers.get(ch, "!") + " "
# print(answer)

#DICTIONARIES with Function

# def new():
#     message = input("> ")
#     words = message.split(' ')
#     emojis = {
#         ":)": "😊",
#         ":(": "🥹"
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + " "   # Checks if word is in emojis; if so, replace it, otherwise keep the original word
#     print(output)
#
# new()

# FUNCTION with PARAMETERS

# def greeting(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Have a good day!")
#
# print("Starting... ")
# greeting (last_name = "Hernandez", first_name = "Kimberly")
# greeting ( "Jose", "Marquez")
# print("Finishing...")

# def calc_cost(total= 50, shipping = 5, discount = 0.1):

# def square(number):
#     return number * number
#
# print (square(3))

# def converter(messsage):
#     """Emoji converter"""
#     words = message.split(' ')
#     emojis = {
#         ":)": "😊",
#         ":(": "🥹"
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + " "   # Checks if word is in emojis; if so, replace it, otherwise keep the original word
#     return output
#
#
# message = input('>')
# result = converter(message)
# print(result)

#
# def favorite_book(book):
#     print(f"One of my favorite books is {book}.")
#
# favorite_book( "Alice in Wonderland" )
#
# def make_shirt(size = 'Large', message = 'I love Python'):
#     print(f"You have provided the size as of {size} and the message to be '{message}'")
#
# make_shirt()
# make_shirt(size= "medium")
# make_shirt("Small", "I love Jesus")
#
# def describe_city(city, country = 'Puerto Rico'):
#     print(f"{city} is in {country}")
#
# describe_city('San Juan')

# def formatted_name(first_name, middle_name, last_name):
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
# musician = formatted_name('Jose', 'Manuel', 'Marquez')
# print(musician)
#
# def build_person (first_name, last_name):
#     person = {'first': first_name, 'last': last_name }
#     return person
#
# persona = build_person('Kimberly', 'Hernandez')
# print(persona)

"""exceptions"""
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print (age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid Value')

# class Dog:
#   def __init__(self, name, age):
#    self.name = name
#    self.age = age
#
#   def sit(self):
#    print(f"{self.name} is now sitting.")
#
#   def roll(self):
#    print(f"{self.name} rolled over!")
#
# my_dog = Dog('Koko', 5)
# your_dog = Dog('Lucy', 3)
#
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
#
# print(f"My dog's name is {your_dog.name}.")
# print(f"My dog is {your_dog.age} years old.")
# your_dog.roll()

# CLASS

# class Restaurant:
#  def __init__(self, restaurant_name, cuisine_type):
#   self.restaurant_name = restaurant_name
#   self.cuisine_type = cuisine_type
#
#  def describe_restaurant(self):
#   print(f"{self.restaurant_name} is a {self.cuisine_type} cuisine type of restaurant.")
#  def open_restaurant(self):
#   print(f"{self.restaurant_name} is now open!")
#
# restaurant = Restaurant('Sushi House', 'Japanese')
# restaurant1 = Restaurant('Chillis', 'American')
# restaurant_2 = Restaurant('Pluckers', 'American')
#
# print(f"I heard good things about {restaurant.restaurant_name}.")
# print (f"How do you like {restaurant.cuisine_type} cuisine?")
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant1.describe_restaurant()
# restaurant_2.describe_restaurant()

#CLASS
class User:
 def __init__(self, first_name, last_name, race, age):
  self.first_name = first_name
  self.last_name = last_name
  self.race = race
  self.age = age

 def describe_user(self):
  print(f"""
Here's what you entered. 
Name: {self.first_name}
Last Name: {self.last_name}
Race: {self.race}
Age: {self.age}
""")
 def greet_user(self):
  print(f"Hello {self.first_name} {self.last_name}!")

user1 = User('Jose', "Marquez", "Hispanic", 24)

user1.describe_user()
user1.greet_user()

