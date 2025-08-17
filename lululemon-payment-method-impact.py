"""
Q1: Between April 1st and June 30th, 2025, what is the count of transactions for each payment method? 
 This analysis will establish the baseline distribution of how customers currently pay.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_transactions

# define the start and end date for Q2 2025
start_date = '2025-04-01'
end_date = '2025-06-30'

# filter the DataFrame for the specified range
q2_2025_transactions = fct_transactions[(fct_transactions['transaction_date'] >= start_date) 
  & (fct_transactions['transaction_date'] <= end_date)].copy()

# group q2_2025_transactions by 'payment_method' then count 'transaction_id' for number of transactions
q2_transaction_counts = q2_2025_transactions.groupby('payment_method')['transaction_id'].count().reset_index()

# rename the column then print result
q2_transaction_counts.rename(columns={'transaction_id': 'transaction_count'}, inplace=True)
q2_transaction_counts


"""
Q2: Between April 1st and June 30th, 2025, what is the average order value for each payment method?
This metric will help us assess which payment methods are tied to higher spending levels.
"""

# filter the DataFrame for the specified range
q2_transaction_avg = fct_transactions[(fct_transactions['transaction_date'] >= start_date) 
   & (fct_transactions['transaction_date'] <= end_date)].copy()

# group q2_transaction_avg by 'payment_method' then calculate the average 'order_value'
q2_transaction_avg = q2_transaction_avg.groupby('payment_method')['order_value'].mean().reset_index()

# rename the column then print result
q2_transaction_avg.rename(columns={'order_value': 'avg_order_value'}, inplace=True)
q2_transaction_avg


"""
Q3: Between April 1st and June 30th, 2025, what would be the predicted sales lift if a 'pay over time' option were introduced?
Assume that 20% of credit card transactions during this period would switch to using the 'pay over time' option.
And that for these switched transactions, the order value is expected to increase by 15% based on 
the average order value of all credit card transactions in that same time period.
"""

# filter the transactions to 'payment_method' == 'credit_card' in the specified date range
q2_2025_cc_transactions = fct_transactions[(fct_transactions['transaction_date'] >= start_date) 
 & (fct_transactions['transaction_date'] <= end_date) 
 & (fct_transactions['payment_method'] == 'credit_card')].copy()

# calculate total numbers of q2_2025_cc_transactions
total_q2_cc_transactions = len(q2_2025_cc_transactions)

# calculate avg order_value for q2_2025_cc_transactions
avg_q2_cc_order = q2_2025_cc_transactions['order_value'].mean()

# predict the number of transactions that would switch to 'pay over time' option
pot_rate = 0.20
switched_transactions = total_q2_cc_transactions * pot_rate

# calculate the expected order_value for the switched_transactions
pot_order_value = 0.15
# the original average order value increased by 15%
avg_pot_order_value = avg_q2_cc_order * (1 + pot_order_value)

# calculate total sales lift
# find the original value of the transactions that switched
original_switched_value = switched_transactions * avg_q2_cc_order

# find the new, higher value of those same transactions
new_switched_value = switched_transactions * avg_pot_order_value

# sales lift is the gain from the new option
sales_lift = new_switched_value - original_switched_value
sales_lift
