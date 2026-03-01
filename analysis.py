import pandas as pd

print("Loading Netflix Dataset...")

data = pd.read_csv('netflix.csv')

print("\nTotal Movies:")
print(data[data['type'] == 'Movie'].shape[0])

print("\nTotal TV Shows:")
print(data[data['type'] == 'TV Show'].shape[0])

print("\nMost Common Genre:")
print(data['listed_in'].mode()[0])

print("\nMovies Released After 2015:")
print(data[data['release_year'] > 2015])

print("\nTop Countries Producing Content:")
print(data['country'].value_counts())

print("Netflix Data Analysis Completed!")