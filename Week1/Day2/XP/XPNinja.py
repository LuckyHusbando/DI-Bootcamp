#Exercise 1

#The PATH Environment Variable
#The PATH environment variable is a system variable that tells your operating system (like Linux, macOS, or Windows) where to look for executable programs when you type a command in the terminal. It contains a list of directories, separated by colons ( : ) on Unix-like systems (Linux, macOS) or semicolons ( ; ) on Windows.

#Exercise 2

#Variables as References

#The core idea is that variables in Python are not containers; they are references (or labels) that point to objects in memory. When you assign a variable, you're essentially attaching a label to an object.

x = [1, 2, 3] # 'x' is a reference to the list object [1, 2, 3]

#You create an alias when you assign an existing variable to a new variable. Both variables will then refer to the same object.

list1 = [10, 20, 30]
list2 = list1 # list2 is now an alias for list1 (they point to the same list object)

print(list1) # Output: [10, 20, 30]
print(list2) # Output: [10, 20, 30]

# Check if they refer to the same object in memory using 'id()'
print(id(list1))
print(id(list2)) # The IDs will be identical

#Exercise 3

True
True
False
False
True
False
X will be True
Y will be False
a will be 5
b will be 10

x is True
y is False
a: 5
b: 10

#Exercise 4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
           Ut enim ad minim veniam, quis nostrud exercitation ullamco \
           laboris nisi ut aliquip ex ea commodo consequat. \
           Duis aute irure dolor in reprehenderit in voluptate velit \
           esse cillum dolore eu fugiat nulla pariatur. \
           Excepteur sint occaecat cupidatat non proident, \
           sunt in culpa qui officia deserunt mollit anim id est laborum."

print.len(my_text)

#Exercise 5

longest_sentence_length = 0
print("Challenge: Type the longest sentence you can without using the letter 'A' (lowercase or uppercase).")
print("Type 'quit' to stop the game.")

while True:
    user_input = input("Enter your sentence: ")

    if user_input.lower() == 'quit':
        print("\nThanks for playing! Your longest valid sentence was", longest_sentence_length, "characters long.")
        break

    # Check if 'A' or 'a' is in the input
    if 'a' in user_input.lower():
        print("Oops! Your sentence contains the letter 'A'. Try again!")
    else:
        current_length = len(user_input)
        if current_length > longest_sentence_length:
            print(f"Congratulations! You've set a new record: {current_length} characters!")
            longest_sentence_length = current_length
        else:
            print(f"Good try! Your sentence was {current_length} characters long. The current record is {longest_sentence_length}.")
