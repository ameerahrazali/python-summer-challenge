"""
Q1: For the month of July 2024, how many transactions did loyalty program members and non-members make?
Compare the transaction counts between these two groups.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_customers

# merge the two DataFrame
merged_df = pd.merge(fct_transactions, dim_customers, on='customer_id', how='inner')

# filter data for July'24
july_2024_transactions = merged_df[(merged_df['transaction_date'].dt.year == 2024) 
  & (merged_df['transaction_date'].dt.month == 7)].copy()

# group july_2024_transactions by 'is_loyalty_member' then count its transactions
july_2024_transactions_count = july_2024_transactions['is_loyalty_member'].value_counts()

# print to compare the two groups
july_2024_transactions_count


"""
Q2: What is the average transaction value for loyalty program members and non-members during July 2024?
Use this to identify which group has a higher average transaction value.
"""

# group july_2024_transactions by 'is_loyalty_member' and calculate the avg of 'transaction_value'
july_2024_transactions_avg = july_2024_transactions.groupby('is_loyalty_member')['transaction_value'].mean().reset_index()

# rename columns for july_2024_transactions_avg
july_2024_transactions_avg.rename(columns={'transaction_value':'avg_transaction_value'}, inplace=True)

# print result
july_2024_transactions_avg


"""
Q3: Determine the percentage difference in average transaction value 
between loyalty program members and non-members for July 2024.
"""

# extract avg transaction values for both member and non from july_2024_transactions_avg
member_avg_value = july_2024_transactions_avg[july_2024_transactions_avg['is_loyalty_member'] == True]['avg_transaction_value'].iloc[0]
non_member_avg_value = july_2024_transactions_avg[july_2024_transactions_avg['is_loyalty_member'] == False]['avg_transaction_value'].iloc[0]

# calculate % diff and use epsilon to prevent division by zero
epsilon = 1e-9
pct_diff = ((member_avg_value - non_member_avg_value) / (non_member_avg_value + epsilon)) * 100

# print the result
print("Average transaction values for July 2024:")
print(f"Loyalty Members: ${member_avg_value:.2f}")
print(f"Non-Members: ${non_member_avg_value:.2f}")
print(f"\nPercentage difference in average transaction value:")
print(f"{pct_diff:.2f}%")
