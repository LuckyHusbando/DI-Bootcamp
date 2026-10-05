#DC - Text Analysis - Week 3 Day 6

import re
import string

class Text:
    """
    A class to analyze text data from a string or a file.
    """
    
    def __init__(self, text):
        """
        Initializes the Text class with a string.
        :param text: The input string.
        """
        self.text = text

    def word_frequency(self, word):
        """
        Counts the occurrences of a specific word in the text.
        :param word: The word to count.
        :return: The count of the word, or None if not found.
        """
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else None

    def most_common_word(self):
        """
        Finds the most frequently occurring word in the text.
        :return: The most common word.
        """
        words = self.text.lower().split()
        if not words:
            return None
        
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
            
        most_common = max(word_counts, key=word_counts.get)
        return most_common

    def unique_words(self):
        """
        Returns a list of unique words in the text.
        :return: A list of unique words.
        """
        words = self.text.lower().split()
        unique_set = set(words)
        return list(unique_set)

    @classmethod
    def from_file(cls, file_path):
        """
        Creates a Text instance from a file.
        :param file_path: The path to the file.
        :return: A new Text instance.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)


class TextModification(Text):
    """
    A class to perform text cleaning, inheriting from Text.
    """
    
    def remove_punctuation(self):
        """
        Removes punctuation from the text.
        :return: The modified text without punctuation.
        """
        return self.text.translate(str.maketrans('', '', string.punctuation))

    def remove_stop_words(self):
        """
        Removes common English stop words from the text.
        :return: The modified text without stop words.
        """
        stop_words = {
            "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", 
            "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", 
            "their", "then", "there", "these", "they", "this", "to", "was", "will", 
            "with"
        }
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        """
        Removes special characters from the text using regex.
        :return: The modified text without special characters.
        """
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)

if __name__ == '__main__':
    # --- Part I: Analyzing a Simple String ---
    print("--- Part I: Analyzing a Simple String ---")
    
    sample_string = "Hello world, this is a simple test. Hello again."
    text_analyzer = Text(sample_string)
    
    # Step 2: word_frequency
    print(f"Frequency of 'hello': {text_analyzer.word_frequency('hello')}")
    print(f"Frequency of 'test': {text_analyzer.word_frequency('test')}")
    print(f"Frequency of 'python': {text_analyzer.word_frequency('python')}")
    
    # Step 3: most_common_word
    print(f"Most common word: {text_analyzer.most_common_word()}")
    
    # Step 4: unique_words
    print(f"Unique words: {text_analyzer.unique_words()}")
    
    print("\n" + "="*50 + "\n")
    
    # --- Part II: Analyzing Text from a File ---
    print("--- Part II: Analyzing Text from a File ---")
    
    # Create a dummy file for demonstration
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write("This is a file test. This file contains some words. Words, words, words.")
        
    # Step 5: from_file
    try:
        file_text_analyzer = Text.from_file('sample.txt')
        print(f"Content from file: {file_text_analyzer.text}")
        print(f"Most common word in file: {file_text_analyzer.most_common_word()}")
        print(f"Frequency of 'words': {file_text_analyzer.word_frequency('words')}")
    except FileNotFoundError:
        print("File 'sample.txt' not found.")
        
    print("\n" + "="*50 + "\n")
    
    # --- Bonus: Text Modification ---
    print("--- Bonus: Text Modification ---")
    
    modification_text = "Hello, world! This is a test, 123. Hello again."
    text_modifier = TextModification(modification_text)
    
    # Step 7: remove_punctuation
    no_punctuation = text_modifier.remove_punctuation()
    print(f"Original text: '{modification_text}'")
    print(f"After removing punctuation: '{no_punctuation}'")
    
    # Step 8: remove_stop_words
    no_stop_words = text_modifier.remove_stop_words()
    print(f"After removing stop words: '{no_stop_words}'")
    
    # Step 9: remove_special_characters
    no_special_chars = text_modifier.remove_special_characters()
    print(f"After removing special characters: '{no_special_chars}'")

    #end