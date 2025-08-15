"""
Q1: There are some data inconsistencies in the 'rating' column, specifically: leading or trailing white space, 
decimals represented by commas instead of decimal points (eg. 4,2 instead of 4.2), and non-numeric values. 
Clean up these data issues and convert the column to a numeric data type.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings

app_ratings_cleaned = app_ratings.copy()

# remove leading/trailing  whitespace
app_ratings_cleaned['rating'] = app_ratings_cleaned['rating'].str.strip()

# replace commas with decimal points
app_ratings_cleaned['rating'] = app_ratings_cleaned['rating'].str.replace(',', '.')

# convert 'rating' from string to numeric
app_ratings_cleaned['rating'] = pd.to_numeric(app_ratings_cleaned['rating'], errors='coerce')

app_ratings_cleaned


"""
Q2: Using the cleaned dataset, display the first and last five entries 
to get an overview of the app ratings across different categories.
"""

# print the first 5 entries of the cleaned DataFrame
print("First five entries of the cleaned app ratings data:")
print(app_ratings_cleaned.head())

# print the last 5 entries of the cleaned DataFrame
print("\nLast five entries of the cleaned app ratings data:")
print(app_ratings_cleaned.tail()) 


"""
Q3: Calculate the basic summary statistics (mean, median, standard deviation) of app ratings 
for each category to identify variations and performance patterns.
"""

# calculate the summary stats for each category 
# group by 'category' and agg() for 'rating' then assign to new DataFrame
cat_summary_stats = app_ratings_cleaned.groupby('category')['rating'].agg(['mean', 'median', 'std']).reset_index()
cat_summary_stats
