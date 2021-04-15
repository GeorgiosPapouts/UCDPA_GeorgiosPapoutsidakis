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


# Sort dining_3 by descending latitude
dining_3_lat = dining_3.sort_values('latitude', ascending=False)

# print the top of the rows
print(dining_3_lat.head())

print(dining_2.head(5))

# inner join of one and two-star-michelin-restaurants on city
name_restaurants_12 = dining_1.merge(dining_2, on='city')
print(name_restaurants_12.head(5))

# detect missing values from three-star-michelin-restaurants
print(dining_3.isna())

print(dining_3.isna().any())

print(dining_3.isna().sum())

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

dining_3.isna().sum().plot(kind='bar')

# Customise the y  and x axis labels
ax.set_ylabel('Number of missing values')
ax.set_xlabel('type of dataset column')
plt.show()











