#Pandas are fancy lists (extended features)

import pandas as pd
data = pd.Series([1, 3, 5, 7, 9])

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

df = pd.read_csv('path/to/your/csvfile.csv')

df.head()  # Displays the first 5 rows by default

ages = df['Age']  # Access the 'Age' column

df.sort_values(by='Age')

df[df['Age'] > 30]  # Selects rows where age is greater than 30

df.groupby('City').mean()  # Groups data by city and calculates mean for each group

#New Challenge

import pandas as pd

data = {
    'Book Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye'],
    'Author': ['F. Scott Fitzgerald', 'Harper Lee', 'George Orwell', 'Jane Austen', 'J.D. Salinger'],
    'Genre': ['Classic', 'Classic', 'Dystopian', 'Classic', 'Classic'],
    'Price': [10.99, 8.99, 7.99, 11.99, 9.99],
    'Copies Sold': [500, 600, 800, 300, 450]
}

df = pd.DataFrame(data)

print("First 5 rows of the DataFrame:")
print(df.head())

print("\nStatistical summary of numerical columns:")
print(df.describe())

print("\nConcise summary of the DataFrame:")
print(df.info())

print("\nDataFrame sorted by Price:")
sorted_by_price = df.sort_values(by='Price')
print(sorted_by_price)

print("\nBooks in the 'Sci-Fi' genre:")
sci_fi_books = df[df['Genre'] == 'Sci-Fi']
print(sci_fi_books)

print("\nBooks with a Price above $17.00:")
expensive_books = df[df['Price'] > 17.00]
print(expensive_books)

print("\nTotal copies sold by each Author:")
copies_by_author = df.groupby('Author')['Copies Sold'].sum().reset_index()
print(copies_by_author)

