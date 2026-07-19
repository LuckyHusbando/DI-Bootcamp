#Mini-Project - Anagram Checker

class AnagramChecker:
    def __init__(self, file_path):
        #Using a set to check the word list is faster.
        self.words = set()

        #Open & read attached word list file
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                #Remove whitespace and store lowercase for consistency
                self.words.add(line.strip().lower())

    def is_valid_word(self, word):
        #Check if user word exists in loaded directory
        return word.lower() in self.words
    
    def is_anagram(self, word1, word2):
        #Convert both words to lowercase for accurate comparison
        w1, w2 = word1.lower(), word2.lower()

        #A word cannot be an anagram of itself
        if w1 == w2:
            return False
        
        #If sorted letters of both words match, they are anagrams
        return sorted(w1) == sorted(w2)
    
    def get_anagrams(self, word):
        #Use list comprehension to find all words in dictionary
        #That are anagrams of the given word
        return [w for w in self.words if self.is_anagram(word, w)]