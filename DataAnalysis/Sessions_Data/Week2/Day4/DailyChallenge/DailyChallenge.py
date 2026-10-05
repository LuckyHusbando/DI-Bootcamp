#Daily Challenge, Challenge 1

# Step 1: Get Input
# Use the input() function to get a string of words from the user.
input_string = input("Enter a comma-separated string of words (e.g., apple,banana,cherry): ")

# Step 2: Split the String
# The str.split() method will separate the input string into a list of words
# using the comma as the delimiter.
words_list = input_string.split(',')

# Step 3: Sort the List
# The sorted() function returns a new list containing all items from the iterable
# in ascending (alphabetical) order.
sorted_words = sorted(words_list)

# Step 4: Join the Sorted List
# The str.join() method concatenates the elements of an iterable into a string.
# The comma is used as the separator.
output_string = ','.join(sorted_words)

# Step 5: Print the Result
print(output_string)

# Expected Output for input 'without,hello,bag,world':
# bag,hello,without,world

#Daily Challenge, Challenge 2

def longest_word(sentence):
    """
    Finds and returns the longest word in a sentence.
    If multiple words have the same maximum length, the first one encountered is returned.
    Punctuation is considered part of the word.
    """
    # Step 2: Split the Sentence into Words
    words = sentence.split()

    # Handle the case of an empty sentence
    if not words:
        return ""

    # Step 3: Initialize Variables
    # Initialize the longest word with the first word in the list
    longest = words[0]

    # Step 4: Iterate Through the Words (starting from the second word)
    for word in words[1:]:
        # Step 5: Compare Word Lengths
        # If the current word's length is greater than the current longest,
        # update the longest word. The problem specifies returning the first
        # one in case of a tie, so we only update on a strictly greater length.
        if len(word) > len(longest):
            longest = word

    # Step 6: Return the Longest Word
    return longest

