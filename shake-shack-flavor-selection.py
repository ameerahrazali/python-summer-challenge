"""
Q1: There was an error in our data collection process, and we unknowingly introduced duplciate rows into our data. 
Remove any duplicate entries in the customer ratings data to ensure the accuracy of the analysis.
"""

milkshake_ratings_cleaned = milkshake_ratings.drop_duplicates().copy()
milkshake_ratings_cleaned


"""
Q2: For each milkshake flavor, calculate the average customer rating and append this as a new column to the milkshake_ratings DataFrame.
Don't forget to clean the DataFrame first by dropping duplicate values.
"""

milkshake_ratings_cleaned = milkshake_ratings.drop_duplicates().copy()

# drop rows with missing 'rating' values
milkshake_ratings_cleaned.dropna(subset=['rating'], inplace=True)

# calculate avg rating for each flavor then assign as new column
# transform() returns a series/df with same size as or ori unlike agg() collapse into each groups
milkshake_ratings_cleaned['avg_flavor_rating'] = milkshake_ratings_cleaned.groupby('flavor')['rating'].transform('mean')
milkshake_ratings_cleaned


"""
Q3: For each row in dataset, calculate the difference between that customer's rating and 
the average rating for the flavor. Don't forget to clean the DataFrame first by dropping duplicate values.
"""

# drop duplicate rows
milkshake_ratings_cleaned = milkshake_ratings.drop_duplicates().copy()

# drop rows with missing 'rating' values
milkshake_ratings_cleaned.dropna(subset=['rating'], inplace=True)

# calculate avg rating for each flavor then assign as new column
milkshake_ratings_cleaned['avg_flavor_rating'] = milkshake_ratings_cleaned.groupby('flavor')['rating'].transform('mean')

# calculate difference rating and avg_flavor_rating
milkshake_ratings_cleaned['rating_diff'] = milkshake_ratings_cleaned['rating'] - milkshake_ratings_cleaned['avg_flavor_rating']

milkshake_ratings_cleaned
