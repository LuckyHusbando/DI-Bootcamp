#MiniProject - Anagram Checker - Week 4, Day 1-3, Anagram Checker

#Remember \n for new lines.

import os

current_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_dir, 'sowpods.txt')

class AnagramChecker:

    def __init__(self, file_path='sowpods.txt'):
            '''Loads the word list from the specific text file.'''
            self.word_list = self._load_word_list(file_path)

    def _load_word_list(self, file_path):
        """
        Helper method to read a text file and return a set of words.
        Using a set for fast lookup is more efficient than a list.
        """
        try:
            with open(file_path, 'r') as file:
                # Stripping whitespace from each line and converting to a set
                return set(word.strip().lower() for word in file)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return set()
        
    def is_valid_word(self, word):
         '''Checks if the given word is in the loaded word list.'''
         return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
         '''Checks if two words are anagrams of each other.'''
         if len(word1) != len(word2) or word1.lower() == word2.lower():
            return False
         
         return sorted(word1.lower()) == sorted(word2.lower())
    
    def get_anagrams(self, word):
        """
        Finds all anagrams for the given word from the word list.
        """
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams
    
    