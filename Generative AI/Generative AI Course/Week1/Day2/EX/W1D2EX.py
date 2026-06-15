#W1D2EX

#Exercise 1

print("Hello world\n" * 4, end="")

#Exercise 2

Calculation = (99**3)*8
print(Calculation)

#Exercise 3

# 5 < 3 #    False
# 3 == 3 #   True
# 3 == "3" # False
# "3" > 3 #  False
# "Hello" == "hello" #  False

#Exercise 4

computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer.")

#Exercise 5

name = "Derek Pursell"
age = 42
shoe_size = 42
info = f"Hi. My name is {name}, I am {age} years old and have a shoe size of {shoe_size} too! My favorite number is also 42!"
print(info)

#Exercise 6

a = 24
b = 12

if a > b:
    print("Hello World!")
else:
    print("Goodbye World!")

#Exercise 7

num = int(input("Enter a number please: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#Exercise 8

yourname = str(input("What is your first name?"))

if yourname is "Derek":
    print("Hey, that's my name!")
else:
    print("It turns out we have different names. So sorry.")

#Exercise 9

RequiredHeight = 145
height = int(input("What is your height in centimeters?"))

if height >= RequiredHeight:
    print("Congrats! You are tall enough to ride the roller coaster!")
else:
    print("I am sorry - You need to grow more before you can ride the roller coaster.")