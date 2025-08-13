### Q1: What is the average spending per guest per visit for each park experience type during July 2024?
# Ensure that park experience types with no recorded transactions are shown with an average spending of 0.0. 
# This analysis helps establish baseline spending differences essential for later segmentation.
# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_guest_spending

# get a list of all unique park_experience_type from the data
all_park_experience = fct_guest_spending['park_experience_type'].unique()

# filter the DataFrame for transactions in July '24 only
july_2024_spending = fct_guest_spending[(fct_guest_spending['visit_date'].dt.year == 2024) & (fct_guest_spending['visit_date'].dt.month == 7)]

# calculate total spend for each guest during a single visit for each park_experience_type
# ['amount_spent'].sum()
spending_per_visit = july_2024_spending.groupby(['park_experience_type', 'guest_id', 'visit_date'])['amount_spent'].sum().reset_index()

# calculate the average spending per guest per visit for each park_experience_type
# and reindex to include all park experience types, filling missing values with 0.0
avg_spending = (spending_per_visit.groupby('park_experience_type')['amount_spent']
                .mean().reindex(all_park_experience, fill_value=0.0).reset_index())

# rename columns avg_spending
avg_spending.columns = ['park_experience_type', 'avg_spent_per_guest_per_visit']

# print final result
print(avg_spending)


### Q2: 
