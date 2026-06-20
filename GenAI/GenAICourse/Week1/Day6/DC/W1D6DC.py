#W1D6DC

#Challenge 1: Letter Index Dictionary

words = input("Please enter a word: ")
letter_indices = {}
for index, char in enumerate(words):
    if char in letter_indices:
        letter_indices[char].append(index)
    else:
        letter_indices[char] = [index]
print(letter_indices)

#Challenge 2: Affordable Items

def buy_items(items_purchase, wallet):
    #Clean wallet string and convert to integer
    #replace() tool swaps symbols for empty space
    clean_wallet = int(wallet.replace("$", "").replace(",", ""))

    #Create empty basket
    basket = []

    #Loop dictionary - items() gives both key and value
    for item_name, price_str in items_purchase.items():

        #Clean price string
        clean_price = int(price_str.replace("$", "").replace(",", ""))

        #Check if money left
        if clean_wallet >= clean_price:
            basket.append(item_name) #Put in basket
            clean_wallet -= clean_price #Subtract cost from wallet

    #Final Output check
    if len(basket) == 0:
            return "Nothing"
    else:
            return sorted(basket) #Returns alphabetical list
        
#Tests

items_1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet_1 = "$300"
print(buy_items(items_1, wallet_1))

items_2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet_2 = "$100"
print(buy_items(items_2, wallet_2))

items_3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet_3 = "$1"
print(buy_items(items_3, wallet_3))