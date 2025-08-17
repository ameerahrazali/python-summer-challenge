"""
Q1: Take a look at the data in the story_date column. Correct any data type inconsistencies in that column.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: stories_data

stories_data_cleaned = stories_data.copy()

# convert 'story_date' to its format
stories_data_cleaned['story_date'] = pd.to_datetime(stories_data_cleaned['story_date'], format='%m/%d/%Y', errors='coerce')
stories_data_cleaned


"""
Q2: Calculate the 25th, 50th, and 75th percentiles of the number of stories created per user per day.
"""

# calculate number of stories created per user per day
stories_per_user_per_day = stories_data_cleaned.groupby(['user_id', 'story_date'])['story_count'].sum().reset_index()

# calculate each percentiles of story_count
percentiles = stories_per_user_per_day['story_count'].quantile([0.25, 0.50, 0.75])
percentiles


"""
Q3: What percentage of users have had at least one day, where they posted more than 10 stories on that day?
"""

# identify users that had at least one day > 10 stories
high_post_users = stories_per_user_per_day[stories_per_user_per_day['story_count'] > 10]['user_id'].unique()

# get total of unique users
total_unique_users = stories_data_cleaned['user_id'].nunique()

# calculate % of high_post_users
pct_high_post_users = (len(high_post_users) / total_unique_users) * 100
pct_high_post_users
