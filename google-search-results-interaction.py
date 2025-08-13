"""
Q1: Identify and remove any duplicate entries in the dataset to ensure data quality. 
How many duplicates were found and removed?
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: user_engagement_data

# identify and count the numbers of duplicate rows
duplicates_found = user_engagement_data.duplicated().sum()

# remove duplicate rows from the DataFrame
user_engagement_data_cleaned = user_engagement_data.drop_duplicates().copy()

# get number of rows after removing duplicates
rows_after_removal = len(user_engagement_data_cleaned)

# print results
print(f"Number of duplicates found and removed: {duplicates_found}")
print(f"Number of rows after removing duplicates: {rows_after_removal}")


"""
Q2: After dropping duplicates, aggregate the data to find the average user interaction time 
for each number of search results displayed per page. What are the average interaction times?
"""

# group the cleaned data by number of search_results_displayed
# then calculate the average interaction_time for each group
avg_interaction_times = user_engagement_data_cleaned.groupby('search_results_displayed')['interaction_time'].mean().reset_index()

# rename columns
avg_interaction_times.columns = ['search_results_displayed', 'average_interaction_time']

# print the result
avg_interaction_times


"""
Q3: Sort the aggregated results from Q2 to determine which number of search results per page 
has the highest average user interaction time. What is the optimal number of search results per page?
"""

# sort the DataFrame by 'average_interaction_time' in desc order
sorted_avg_interaction_times = avg_interaction_times.sort_values(by='average_interaction_time', ascending=False).reset_index(drop=True)

# print the result
sorted_avg_interaction_times
