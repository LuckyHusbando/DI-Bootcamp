#W3D6DC

#Daily Challenge

import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        #Split text string into word list
        word_list = self.text.split()

        #Count how many times a word appears
        count = word_list.count(word)

        #Return count or a message if not found
        if count > 0:
            return count
        else:
            return f"The word '{word}' was not found in the text."
        
    def most_common_word(self):
        #Split text into list of words
        words = self.text.split()

        if not words:
            return None #Handles case where text is empty
        
        #Use dictionary to store word frequencies
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        #Find word with highest frequency
        most_common = max(word_counts, key=word_counts.get)

        #Return the most common word
        return most_common
    
    def unique_words(self):
        #Split text into list of words
        words = self.text.split()

        #Use set to store unique words
        unique_set = set(words)

        #Return unique words as list
        return list(unique_set)
    
    @classmethod
    def from_file(cls, file_path):
        #Open file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            #Read file content
            content = file.read()

        #Create and return a Text instance
        return cls(content)

# MOVED THIS OUTSIDE OF THE TEXT CLASS
class TextModification(Text):
    
    def remove_punctuation(self):
        #Create translation table that maps all punctiation to None
        translator = str.maketrans('', '', string.punctuation)
        modified_text = self.text.translate(translator)
        return modified_text
    
    def remove_stop_words(self):
        #A predefined set of common English stop words
        stop_words = {"a", "an", "the", "and", "but", "if", "or", "because", "as", "what",
                      "is", "in", "to", "of", "it", "that", "this", "for", "on", "with"}
        
        #Split into words
        words = self.text.split()

        #Keep word only if lowercase version is NOT in the stop_words set
        filtered_words = [word for word in words if word.lower() not in stop_words]

        #Join back into string
        modified_text = " ".join(filtered_words)
        return modified_text
    
    def remove_special_characters(self):
        # The regex pattern [^A-Za-z0-9\s] means:
        # ^      = NOT
        # A-Za-z = Letters
        # 0-9    = Numbers
        # \s     = Whitespace
        # So, it replaces anything that is NOT a letter, number, or space with ''
        modified_text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return modified_text
    
if __name__ == "__main__":
    #Create instance of new class
    my_modifier = TextModification("Hello, World! @Python is the #1 language for me!")
    print("No Punctuation:  ", my_modifier.remove_punctuation())
    print("No Stop Words:   ", my_modifier.remove_stop_words())
    print("No Special Chars:", my_modifier.remove_special_characters())