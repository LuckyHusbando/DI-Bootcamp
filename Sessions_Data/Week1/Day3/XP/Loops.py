#LOOPS

fruits = ['apple', 'banana', 'kiwi', 'pear']

for fruit in fruits: fruits = [['apple', 'banana', 'kiwi', 'pear']]
print (fruits)

#Sequences that we can loop through
# Strings 

for char in 'Harry':
    print(char)

#List: example above
#for <variable> in <sequence>:

#Tuples & Sets

languages = ('PT', 'ES', 'IT')
for lang in languages:
    print(lang)

#Range()

for i in range(0,11,2):
    print('Hello', i)

#A range is required in any sequence

#for i in enumerate(fruits):
    #if fruit == 'apple':
        #fruits[i] = 'Windows is better'
    #else:     

#Try Wire Loop exercises next time

#Important build in function used in "for" loops:
#range(start, stop, step)
#enumerate()
#Useful for when the amount of loops is known/specific

#====While Loops====
#Useful for reiterating a code loop until a specific condition is True

i = 0
while i < len(fruits):
    print(i)
    i += 1