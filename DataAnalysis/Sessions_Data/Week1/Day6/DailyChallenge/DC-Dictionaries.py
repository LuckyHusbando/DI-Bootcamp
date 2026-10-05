#Challenge 1 - Character Indexer

# 1. User Input: Ask the user to enter a word.
word = input("Enter a word: ")

# 2. Create the dictionary
letter_indices = {}

# Iterate through each character of the word with its index
for index, char in enumerate(word):
    # If the character is already a key, append the index to its list
    if char in letter_indices:
        letter_indices[char].append(index)
    # Otherwise, create a new key with a list containing the current index
    else:
        letter_indices[char] = [index]

# 3. Print the final dictionary
print(letter_indices)

#Challenge 2 - Affordable Items

def find_affordable_items(items_purchase, wallet):
    """
    Calculates and returns a sorted list of items that can be purchased
    with a given amount of money.
    """
    # 2. Data Cleaning: Clean and convert the wallet amount to an integer
    # Remove '$' and ',' then convert to an integer
    wallet_amount = int(wallet.replace('$', '').replace(',', ''))
    
    # Clean and convert the item prices to integers in a new dictionary
    cleaned_prices = {
        item: int(price.replace('$', '').replace(',', ''))
        for item, price in items_purchase.items()
    }
    
    # 3. Determining Affordable Items:
    affordable_items = []
    for item, price in cleaned_prices.items():
        if price <= wallet_amount:
            affordable_items.append(item)
            
    # 4. Sorting and Output:
    if not affordable_items:
        return "Nothing"
    else:
        return sorted(affordable_items)

# --- Examples ---

# Example 1
items_purchase_1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet_1 = "$300"
print(f"Items you can buy with {wallet_1}: {find_affordable_items(items_purchase_1, wallet_1)}")

# Example 2
items_purchase_2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet_2 = "$100"
print(f"Items you can buy with {wallet_2}: {find_affordable_items(items_purchase_2, wallet_2)}")

# Example 3
items_purchase_3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet_3 = "$1"
print(f"Items you can buy with {wallet_3}: {find_affordable_items(items_purchase_3, wallet_3)}")
