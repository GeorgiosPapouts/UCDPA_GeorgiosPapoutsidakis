import pandas as pd

# Import the one-star-michelin-restaurants.csv data: dining_1
dining_1 = pd.read_csv('one-star-michelin-restaurants.csv')

# print out dining_1
print(dining_1)

# Import the one-star-michelin-restaurants.csv data: dining_2
dining_2 = pd.read_csv('two-stars-michelin-restaurants.csv')

# print out dining_2
print(dining_2)

# Import the one-star-michelin-restaurants.csv data: dining_3
dining_3 = pd.read_csv('three-stars-michelin-restaurants.csv')

# print out dining_3
print(dining_3)

# Fix import by including index_col
dining_1 = pd.read_csv('one-star-michelin-restaurants.csv', index_col=1)

# print out dining_1
print(dining_1)

# Print out name column as Pandas Series
print(dining_1['name'])