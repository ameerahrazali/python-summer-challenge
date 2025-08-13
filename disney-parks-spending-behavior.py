"""
Q1: What is the average spending per guest per visit for each park experience type during July 2024?
Ensure that park experience types with no recorded transactions are shown with an average spending of 0.0. 
This analysis helps establish baseline spending differences essential for later segmentation.
Note: pandas and numpy are already imported as pd and np
The following tables are loaded as pandas DataFrames with the same names: fct_guest_spending
"""

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


"""
Q2: For guests who visited our parks more than once in August 2024, 
what is the difference in spending between their first and their last visit?
This investigation, using sequential analysis, will reveal any shifts in guest spending behavior over multiple visits.
"""

 # filter the DataFrame for transactions in August '24 only
august_2024_spending = fct_guest_spending[(fct_guest_spending['visit_date'].dt.year == 2024) & (fct_guest_spending['visit_date'].dt.month == 8)]

# get guests in Aug '24
visit_counts = august_2024_spending.groupby('guest_id')['visit_date'].nunique()
# get guests in Aug '24 visit_counts>1 - visit more than once
repeat_guests = visit_counts[visit_counts > 1].index  # .index to return the index value (guest_id) of series

# filter the data to only include only repeat_guests
repeat_guest_spending = august_2024_spending[august_2024_spending['guest_id'].isin(repeat_guests)]

# calculate total spending per guest per visit
spending_per_visit = repeat_guest_spending.groupby(['guest_id', 'visit_date'])['amount_spent'].sum().reset_index()

# sort data by visit_date to find first and last visits
spending_per_visit.sort_values(by=['guest_id', 'visit_date'], inplace=True)

# find spending for first and last visit for each guest
first_visit_spending = spending_per_visit.groupby('guest_id')['amount_spent'].first()  # find first visit
last_visit_spending = spending_per_visit.groupby('guest_id')['amount_spent'].last()  # find first visit

# calculate the difference and assign to final DataFrame
spending_difference = (last_visit_spending - first_visit_spending).reset_index()
spending_difference.rename(columns={0: 'spending_diff_last_and_first'}, inplace=True)
print(spending_difference)


"""
Q3: In September 2024, how can guests be categorized into distinct spending segments
such as Low, Medium, and High based on their total spending? Use the following thresholds for categorization:
-Low: Includes values from $0 up to, but not including, $50.
-Medium: Includes values from $50 up to, but not including, $100.
-High: Includes values from $100 and above.
Exclude guests who did not make any purchases in the period.
"""

# filter the DataFrame for transactions in Sept '24 only
sept_2024_spending = fct_guest_spending[(fct_guest_spending['visit_date'].dt.year == 2024) & (fct_guest_spending['visit_date'].dt.month == 9)]

# calculate total spending each guest in Sept '24
total_guest_spending = sept_2024_spending.groupby('guest_id')['amount_spent'].sum().reset_index()
total_guest_spending.rename(columns={'amount_spent':'total_sept_spending'}, inplace=True)

# define the spending thresholds and labels for the 3 categorizations
bins = [0, 50, 100, float('inf')]
labels = ['Low', 'Medium', 'High']

# categorize each guest's total spending using pd.cut() - segment and sort data values into discrete intervals (bins)
total_guest_spending['spending_segment'] = pd.cut(total_guest_spending['total_sept_spending'], bins=bins, labels=labels, right=False)
# right=False ensures the bins are [0, 50), [50, 100), [100, inf)

# print the final DataFrame
print(total_guest_spending)




