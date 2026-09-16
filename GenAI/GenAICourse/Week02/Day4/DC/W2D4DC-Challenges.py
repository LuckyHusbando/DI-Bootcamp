#W2D4DC

#Daily Challenge - Challenges

#===Challenge 1 - Sorting===

#Define program
def sort_csv_words():

#Step 1: Get Input

#Store user's text inside variable 'user_input'
    user_input = input("Enter words separated by commas: ")

#Step 2: Split the String

#Chop string into list of strings

    words_list = user_input.split(',')

#Step 3: Sort the List

#Sort list in-place (alphabetically)
    words_list.sort()

#Step 4: Join the Sorted List

#Glue list back together with commas
    sorted_string = ", ".join(words_list)

#Step 5: Print Result

    print(sorted_string)

#Run Program

if __name__ == "__main__":
    sort_csv_words()

#===Challenge 2 - Longest Word===

#Step 1: Define Function

def find_longest_word(sentence):

#Step 2: Split Sentence into Words

    words = sentence.split()

#Step 3: Initialize Variables

    longest_word = ""

#Step 4: Iterate through Words

    for word in words:

#Step 5: Compare Word Lengths

    #Using strict > inequality to handle ties
        if len(word) > len(longest_word):
            longest_word = word

#Step 6: Return Longest Word

    return longest_word

#Test Function

if __name__ == "__main__":
    example_sentence = "The quick brown fox jumped over the lazy dog."
    result = find_longest_word(example_sentence)
    print(f"The longest word is: {result}")
    #Output: jumped

    tie_sentence = "A apple, banana, and cherry tree."
    result_tie = find_longest_word(tie_sentence)
    print(f"The tie-breaker winner is: {result_tie}")
    #Output: apples, (Because 'apples,' has six characters and came first!)

