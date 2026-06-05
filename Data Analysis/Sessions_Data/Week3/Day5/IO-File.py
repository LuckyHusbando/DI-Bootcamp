#Input/Output - I/O

import os

#The Old Way of Opening files:

# f = open('secrets.txt')
# secret_data = f.read()
# # secret_data is a string
# f.close()

#The Modern Way:

# with open("secrets.txt",encoding = 'utf-8') as f:

#How to read a file:

# Will search the directory for the file - -----------------##ESSENTIAL CODE##---------------------
dir_path = os.path.dirname(os.path.realpath(__file__)) 
print('dir path: ', dir_path)

with open(f'{dir_path}\Secrets.txt', 'r', encoding='utf-8') as file_obj:
    file_content = file_obj.read()

#     print(file_content)

#Star Wars Exercise

# Read the file line by line
with open(f'{dir_path}\starwars.txt', 'r', encoding='utf-8') as f:
    txt_list = f.readlines()
    for line in txt_list:
        print(line)
    print('end of document')

# Read only the 5th line of the file
print(txt_list[4])

# Read only the 5 first characters of the file
print(txt_list[0][:4])

# Read all the file and return it as a list of strings. Then split each word into letters
#Using list comprehension
temp = [list(line) for line in txt_list]
print(temp)

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
counts = {'Darth':0, 'Luke': 0, 'Lea': 0}
for line in txt_list:
    line = line.strip()
    if line == 'Darth':
        counts['Darth'] += 1
    elif line == 'Luke':
        counts['Luke'] += 1
    elif line == 'Lea':
        counts['Lea'] += 1
print(counts)

# Append your first name at the end of the file
with open(f'{dir_path}\starwars.txt', 'a', encoding='utf-8') as f:
    # f.seek(0) #the cursor goes to the beginning of the file.
    f.seek(0, os.SEEK_END) #We make sure the cursor is at the end of the file.
    f.write('\nDerek')
    print("Successfully added")

# Append "SkyWalker" next to each first name "Luke"

# for i, name in enumerate(txt_list):
#     if name.strip() == 'Luke':
#         txt_list[i] = f'{name} Skywalker'
# print("Successfully changed.")
# --This doesn't work! Oops! You can't edit it this way.--
#You need to copy the content, change it, then overwrite the content you changed.

modified_lines = []
for line in txt_list:
    if line.strip() == "Luke":
        modified_lines.append('Luke Skywalker\n')
    else:
        modified_lines.append(line)

#Challenge: Transform the code above into List Comprehension

with open(f'{dir_path}\starwars.txt', 'w', encoding='utf-8') as f:
    f.seek(0) #Make sure the cursor is at the beginning of the file.
    f.writelines(modified_lines)

#List Comprehension Method

modified_lines = ['Luke Skywalker\n' if line.strip() == 'Luke' else line for line in txt_list]