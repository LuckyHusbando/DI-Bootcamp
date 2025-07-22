# Data Structures: Sequences

#TUPLES

#Tuples cannot be changed!
#They are used for listing data that is considered permanent.
#Countries, ID numbers, Key Accounts, etc.

my_id = (1234)

#Tuples can never be empty!

my_tuple = (1,)
print(type(my_tuple))

nums = [1,2,34,5,67]
nums_tuple = tuple(nums)
print(nums_tuple)

#Tuple Methods
cities = ('NYC', 'Boston,' 'SP', 'RJ', 'NYC')

print(cities.count('NYC'))

#We can use Index
print(cities[1])
#Disregard - print(cities.index('SP'))

# This can't be done, Tuples cannot be appended - cities[1] = 'RJ'

#Unpacking

languages = ('EN', 'RU', 'JP', 'HE')

lang1, lang2, lang3, lang4 = languages
print(lang1)

#SETS - Sequences that cannot have duplicated values and it is not ordered
#They are useful for avoiding duplicated elements.

some_set = set()
other_set = {1,2,6}

Countries = {"Israel", "US", "Brazil"}
Names = {"Shimon", "Israel", "David"}

set_3 = Countries.intersection(Names)
print(set_3)

merged_set = Countries.union(Names)
print(merged_set)

dif_set = Countries.difference(Names)
print(dif_set)
