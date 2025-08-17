"""
Q1: How many transactions in October 2024 have a customer email ending with a domain other than 'gmail.com', 'yahoo.com', or 'hotmail.com'? 
This metric will help us identify transactions associated with less common email providers that may indicate emerging risk patterns.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions, dim_risk_flags

# define standard email domains 
std_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']

# filter transactions for Oct'24
oct_2024_transactions = fct_transactions[(fct_transactions['transaction_date'].dt.year == 2024) 
  & (fct_transactions['transaction_date'].dt.month == 10)].copy()

# identify transactions with email domains not in std_domains
not_std_domains = ~oct_2024_transactions['customer_email'].str.endswith(tuple(std_domains))

# count the number of not_std_domains
not_std_domains_count = oct_2024_transactions[not_std_domains].shape[0]
not_std_domains_count


"""
Q2: For transactions occurring in November 2024, what is the average transaction amount, using 0 as a default for any missing values? 
This calculation will help us detect abnormal transaction amounts that could be related to fraudulent activity.
"""

 # filter transactions for Nov'24
nov_2024_transactions = fct_transactions[(fct_transactions['transaction_date'].dt.year == 2024) 
  & (fct_transactions['transaction_date'].dt.month == 11)].copy()

# handle missing values in 'transaction_amount' with .fillna(0)
nov_2024_transactions['transaction_amount'].fillna(0, inplace=True)

# calculate avg of transaction_amount
avg_nov_2024_transactions = nov_2024_transactions['transaction_amount'].mean()
avg_nov_2024_transactions


"""
Q3: Among transactions flagged as 'High' risk in December 2024, which day of the week recorded 
the highest number of such transactions? This analysis is intended to pinpoint specific days with concentrated high-risk activity
and support the development of our preliminary fraud detection score.
"""

# merge the two DataFrame 
merged_df = pd.merge(fct_transactions, dim_risk_flags, on='transaction_id', how='inner')

# filter transactions for Dec'24
dec_2024_high_risk = merged_df[(merged_df['transaction_date'].dt.year == 2024) 
  & (merged_df['transaction_date'].dt.month == 12) 
  & (merged_df['risk_level'] == 'High')].copy()

# extract day of week from transaction_date
dec_2024_high_risk['day_of_week'] = dec_2024_high_risk['transaction_date'].dt.day_name()

# count number of high risk by day_of_week
daily_high_risk_counts = dec_2024_high_risk.groupby('day_of_week').size().reset_index(name='transaction_count')

# sort daily_high_risk_counts in descending order
daily_high_risk_sorted = daily_high_risk_counts.sort_values(by='transaction_count', ascending=False)

# print result for highest day of transaction
print(daily_high_risk_sorted.iloc[0])
