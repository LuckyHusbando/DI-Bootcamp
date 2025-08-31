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

pd.merge(df1, df2, on='common_column')
