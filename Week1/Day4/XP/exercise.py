#Exercise 1 - Favorite Numbers

my_fav_numbers = {8, 2, 48, 23, 48, 42, 31, 20}
my_fav_numbers.add(34)
my_fav_numbers.add(84)
my_fav_numbers.remove(84)

friend_fav_numbers = {82, 53, 72, 91, 24, 62, 3}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2 - Tuples

my_tuple = (34, 56, 24, 43, 59)
#Tuples cannot be edited by commands under normal circumstances.

#Exercise 3 - List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(1, "Apples")
basket.count("Apples")
basket.clear
print(basket)

#Exercise 4 - Floats

#A float is a real number that contains a fractional park, like including a decimal point.
#This is different from an integer which is simply a whole number.

My_Floats = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(My_Floats)

#Exercise 5 - For Loop

Test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in Test_numbers:
    print(num)

for index, element in enumerate(Test_numbers):
    if index % 2 == 0:
        print(f'Index: {index}, Element: {element}')

#Exercise 6 - While Loop

my_name = "Derek"
user_name = ""

while user_name != my_name:
    user_name = input("Please enter your real name: ")

print(f"Hello, {my_name}! You have entered the correct name!")

#Exercise 7 - Favorite Fruits



#Exercise 8 - Pizza Toppings

#Exercise 9 - Cinemax Tickets

#Exercise 10 - Sandwich Orders

