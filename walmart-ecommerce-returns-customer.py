"""
Q1: Identify and list all unique customer IDs who have made returns between July 1st 2024 and June 30th 2025. 
This will help us understand the base set of customers involved in returns during the specified period.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: customer_returns

customer_returns_cleaned = customer_returns.copy()

# coerce nulls to NaT
customer_returns_cleaned['order_date'] = pd.to_datetime(customer_returns_cleaned['order_date'], errors='coerce')

# define date range for filtering
start_date = '2024-07-01'
end_date = '2025-06-30'

# filter DataFrame to include only returns that True within date range
return_customers = customer_returns_cleaned[(customer_returns_cleaned['order_date'] >= start_date) 
  & (customer_returns_cleaned['order_date'] <= end_date) 
  & (customer_returns_cleaned['return_flag'] == True)].copy()

# extract and list unique customer_id from return_customers
unique_return_customer_id = return_customers['customer_id'].unique()
unique_return_customer_id


"""
Q2: Convert the 'order_date' column to a datetime format and create a MultiIndex with 'customer_id' and 'order_date'.
Then, calculate the total number of returns per customer for each month. 
This will provide insights into monthly return patterns for each customer.
"""

customer_returns_cleaned = customer_returns.copy()

# convert 'order_date' to datetime and coerce nulls to NaT
customer_returns_cleaned['order_date'] = pd.to_datetime(customer_returns_cleaned['order_date'], errors='coerce')

# filter to where 'return_flag' is True only & drop any nulls
returned_items = customer_returns_cleaned[(customer_returns_cleaned['return_flag'] == True) 
  & (customer_returns_cleaned['order_date'].notnull())].copy()

# set MultiIndex with 'customer_id' & 'order_date'
returned_items.set_index(['customer_id', 'order_date'], inplace=True)

# group by 'customer_id' level and use pd.Grouper to level 'order_date' too
monthly_returns = (returned_items.groupby(['customer_id', pd.Grouper(level='order_date', freq='M')])
  .agg(total_monthly_returns=('return_flag', 'sum')).reset_index())   # count return_flag=True then assign to new series

# total number of returns per customer for each month
monthly_returns
