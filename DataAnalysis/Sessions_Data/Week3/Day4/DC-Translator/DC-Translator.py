#DC - Translator - Week 3 Day 4

from googletrans import Translator

def translate_french_words(words):
    """
    Translates a list of French words to English and returns a dictionary.
    
    Args:
        words (list): A list of French words.
        
    Returns:
        dict: A dictionary with French words as keys and English translations as values.
    """
    translator = Translator()
    translation_dict = {}

    for word in words:
        # Translate the word to English
        translation = translator.translate(word, src='fr', dest='en')
        
        # Add the original word and its translation to the dictionary
        translation_dict[word] = translation.text
    
    return translation_dict

# The list of French words
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Get the translated dictionary
translated_result = translate_french_words(french_words)

# Print the result
print(translated_result)