# numbers = [1, 2, 3, 4, 2, 3, 5, 6, 6]
# repetition = []
#
# for number in numbers:
#     if number not in repetition:
#         repetition.append(number)
# print(repetition)
#
#
#
# list_one = [4, 5, 7, 7, 9, 5, 4, 8]
# item = []
#
# for repeat in list_one:
#     if repeat not in item:
#         item.append(repeat)
# print (item)
#
#
# print ('Jose es una ratica')

# number = [2, 4, 5, 5, 4, 3, 2, 5, 7, 6, 9, 3, 4, 8, 6, 2, 3]
# repetition = []
#
# for number_one in number:
#     if number_one not in repetition:
#         repetition.append(number_one)
#         repetition.sort()
# print(repetition)


# my_tuple = (1, 2, 3, 4, 5)
# a, b, _, d, e = my_tuple
# a, b, *numbers = my_tuple
#
# nested_dict = {
#     'person': {'name': 'Alice', 'age': 30},
#     'location': 'New York'
# }
#
# print(nested_dict['name'])  # Output: Alice


#Nested loops/ for loops
# for x in range(4):
#     for y in range(2):
#         print(f'({x}), ({y})')

# count = 0
# for x in range(1, 10):
#   if x % 2 == 0:
#       count += 1
#       print (x)
# print (f"we have {count} even numbers.")


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reader = 0
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reader} miles on it.")
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#     def update_odometer(self, mileage): #will update the existing miles
#         if mileage >= self.odometer_reader:
#             self.odometer_reader = mileage
#         else:
#             print("You can't roll back odometer!")
#     def increase_odometer(self, miles): #increase the miles
#         if miles > 0:
#             self.odometer_reader += miles
#         else:
#             print("You can't roll back odometer!")
#
# my_new_car = Car('Toyota', 'GR86', '2022')


# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reader = 20
# my_new_car.read_odometer()
#

# my_new_car.update_odometer(40)
# my_new_car.read_odometer()
# my_new_car.increase_odometer(20)
# my_new_car.read_odometer()
# my_new_car.increase_odometer(-20)
# my_new_car.read_odometer()

#Restaurant



