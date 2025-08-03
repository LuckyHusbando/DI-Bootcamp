#Timed Challenge 1

def reverse_sentence(sentence):
    """Reverses a sentence word by word."""
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Reverse the order of the words in the list
    reversed_words = words[::-1]
    
    # Join the reversed list of words back into a single string
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence

# The input sentence
input_sentence = "You have entered a wrong domain"

# Get the reversed sentence
output_sentence = reverse_sentence(input_sentence)

# Print the original and the reversed sentences
print(f"Input: {input_sentence}")
print(f"Output: {output_sentence}")

print(reversed)