#Data Structures
#A data structure is a way of storing and organizing data according to a certain format or structure.
#Data structures in Python include Lists, Tuples, Dictionaries, and Sets
#Let's take a look at Lists today.

user_name = 'Derek'
email = 'Derek@gmail.com'
user_age = 35
Is_Online = True

User_info = [user_name, email, user_age, Is_Online]

#Commas separate elements and are very important.

print(len(User_info))

some_list = list('item 1') #Create a list with the function
other_list = ['item 1']

print(some_list)
print(other_list)

Empty_list = []

print(User_info[2])

fruits = ['orange', 'kiwi', 'apple', 'lime']
#Slice
print(fruits[-2:])

fruits[1] = 'pineapple'
print(fruits)

my_name = "Derek"
#typeError: not possible to change an item on a strings, strings are immutable.

#list methods
#Methods are functions that you can apply to a specific class or type
fruits = ['orange', 'kiwi', 'apple', 'lime']
fruits.insert(1, 'mango')
print(fruits)

fruits.remove('kiwi') #Used often
print(fruits)

fruits.append('watermelon') #Append is used often
print(fruits)

fruits.pop() #With no argument, it deletes the last element.
print(fruits)

Vegetables = ['tomato', 'potato', 'carrot']
colors = ['red', 'blue', 'green']

fruits.extend(Vegetables)
print (fruits)

#Sorted() and .sort()
fruits_sorted = sorted(fruits)
print(fruits)
print(fruits_sorted)

fruits.sort()
print(fruits)

#Exercise 1

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1: 
    index_20 = list1.index(20)
    list1[index_20] = 200
print(list1)
