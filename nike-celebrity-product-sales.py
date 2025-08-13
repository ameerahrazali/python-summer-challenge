"""
Q1: For Q1 2025 (January 1st through March 31st, 2025), can you identify all records of celebrity collaborations from the sales data 
where the sale_amount is missing? This will help us flag incomplete records that could impact the analysis of Nike's product performance.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_sales

# define the start and end dates for Q1 2025
start_date = '2025-01-01'
end_date = '2025-03-31'

# filter the DataFrame for Q1 '25
q1_2025_sales = fct_sales[(fct_sales['sale_date'] >= start_date) & (fct_sales['sale_date'] <= end_date)]

# identify records within q1_2025_sales where 'sale_amount' is null
missing_amount_records = q1_2025_sales[q1_2025_sales['sale_amount'].isnull()]

# print the result 
missing_amount_records


"""
Q2: For Q1 2025 (January 1st through March 31st, 2025), can you list the unique combinations of celebrity_id and product_id from the sales table? 
This will ensure that each collaboration is accurately accounted for in the analysis of Nike's marketing performance.
"""

 # get the unique combinations of celebrity_id and product_id
unique_collab = q1_2025_sales[['celebrity_id', 'product_id']].drop_duplicates().reset_index(drop=True)

# print the result
unique_collab


"""
Q3: For Q1 2025 (January 1st through March 31st, 2025), can you rank the unique celebrity collaborations based on their total sales amounts
and list the top 3 collaborations in descending order? This will help recommend the most successful partnerships for Nike's future product drop strategies.
"""

 # group the filtered data by celebrity_id and product_id to get total sales for each collab
collab_sales = q1_2025_sales.groupby(['celebrity_id', 'product_id'])['sale_amount'].sum().reset_index()

# sort the collaborations in descending order based on their total sales
top_collab = collab_sales.sort_values(by='sale_amount',ascending=False)

# Select the top 3 collaborations
top_3_collab = top_collab.head(3)

# print the result
top_3_collab
