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

# Customise the y  and x axis  and graph labels
ax.set_ylabel('Number of missing values')
ax.set_xlabel('type of dataset column')
# Add the title
ax.set_title('Missing values for columns data')
plt.show()

# Fill all the missing values with 0 in dining_3

dining_3_filled = dining_3.fillna(0)
print(dining_3_filled)

# Use slicing to get columns 7 to 8 from dining_2
print(dining_2.iloc[:, 7:9])


# Use the for loop
michelin_1 = {'Bar Crenn' : 37.8,
              'Nouri' : 1.28086,
              'Fiola' :  38.9 }
for key, value in michelin_1.items() :
    print(key + 'has' + 'latitude' + str(value))

# Import dining_1 data
import pandas as pd
dining_1_1 = pd.read_csv('one-star-michelin-restaurants.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in dining_1_1.iterrows() :
    print(lab)
    print(row.head(10))


# build DataFrame of names and cities from dining_2
df_2 = pd.DataFrame(dining_2, columns=['name', 'city'])
print(df_2.head(10))

# build DataFrame of names and cities from dining_3
df_3 = pd.DataFrame(dining_3, columns=['name', 'region'])
print(df_3.head(12))

# join DataFrames df_2 and df_3
Joined_data = pd.merge_ordered(df_3, df_2, on='name', fill_method='ffill')
print(Joined_data)

# Pivot for mean latitude for each year for dining_2
mean_latitude_by_year = dining_2.pivot_table(values = 'latitude', index = 'year')

# Print mean_latitude_by_year
print(mean_latitude_by_year)

# Import package
import numpy as np

# Pivot for mean and median latitude for each year for dining_2
mean_med_latitude_by_year = dining_2.pivot_table(values = 'latitude', index = 'year', aggfunc = [np.mean, np.median])

# print mean_med_latitude_by_year
print(mean_med_latitude_by_year)

# Pivot for mean latitude for each year for dining_1
mean_latitude_by_year = dining_1.pivot_table(values = 'latitude', index = 'year')

# Print mean_latitude_by_year
print(mean_latitude_by_year)

# Import package
import numpy as np

# Pivot for mean and median latitude for each year for dining_1
mean_med_latitude_by_year = dining_1.pivot_table(values = 'latitude', index = 'year', aggfunc = [np.mean, np.median])

# print mean_med_latitude_by_year
print(mean_med_latitude_by_year)

# Pivot for mean latitude for each year for dining_3
mean_latitude_by_year = dining_3.pivot_table(values = 'latitude', index = 'year')

# Print mean_latitude_by_year
print(mean_latitude_by_year)

# Import package
import numpy as np

# Pivot for mean and median latitude for each year for dining_3
mean_med_latitude_by_year = dining_3.pivot_table(values = 'latitude', index = 'year', aggfunc = [np.mean, np.median])

# print mean_med_latitude_by_year
print(mean_med_latitude_by_year)

dining_traits = ['Ikarus', 2019, 'latitude', 'longitude', 'city', 'region', 'zipCode', 'cuisine', 'price', 'url']
print(dining_traits.append('url'))


# Create a list of dictionaries with new data
dining_3_list = [
    {'name': 'Alinea', 'longitude': -87.6480, 'city': 'Chicago'}, {'name': 'Le Bernardin', 'longitude': 8561348, 'city': 'New York'},
]

# Convert list into DataFrame
dining_3_2019 = pd.DataFrame(dining_3_list)

# Print the new DataFrame
print(dining_3_2019)

# Import the two-star-michelin-restaurants.csv data: dining_2
dining_2 = pd.read_csv('two-stars-michelin-restaurants.csv', index_col=0)
import matplotlib.pyplot as plt
import seaborn as sns

g=sns.catplot(y='region',
            data=dining_2,
            kind='count')
g.fig.suptitle('Number of restaurants awarded two michelin stars')
plt.show()

# Import the three-star-michelin-restaurants.csv data: dining_3
dining_3 = pd.read_csv('three-stars-michelin-restaurants.csv', index_col=0)
import matplotlib.pyplot as plt
import seaborn as sns

g=sns.catplot(y='region',
            data=dining_3,
            kind='count')
g.fig.suptitle('Number of restaurants awarded three michelin stars')
plt.show()

# Import the one-star-michelin-restaurants.csv data: dining_1
dining_1 = pd.read_csv('one-star-michelin-restaurants.csv', index_col=0)
import matplotlib.pyplot as plt
import seaborn as sns

g=sns.catplot(y='region',
            data=dining_1,
            kind='count')
g.fig.suptitle('Number of restaurants awarded one michelin star')
plt.show()

# Import the one-star-michelin-restaurants.csv data: dining_3
import matplotlib.pyplot as plt

# Plot a bar chart of the latitude of the three-stars-michelin-restaurants
dining_3 = pd.read_csv('three-stars-michelin-restaurants.csv', index_col=0)
fig, ax = plt.subplots()
ax.bar(dining_3.index, dining_3['latitude'])
ax.set_xticklabels(dining_3.index, rotation=90)
ax.set_ylabel('Latitude')
plt.show()

# Plot a bar chart of the longitude of the three-stars-michelin-restaurants
dining_3 = pd.read_csv('three-stars-michelin-restaurants.csv', index_col=0)
fig, ax = plt.subplots()
ax.bar(dining_3.index, dining_3['longitude'])
ax.set_xticklabels(dining_3.index, rotation=90)
ax.set_ylabel('Longitude')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x='latitude',
                y='longitude',
                data=dining_3,
                hue='region')
plt.show()




































