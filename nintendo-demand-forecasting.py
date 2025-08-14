"""
Q1: What percentage of records have missing values in at least one column? 
Handle the missing values, so that we have a cleaned dataset to work with.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: pre_sale_data

# data issues: missing values in column region & demographic_group

# calculate the total number of records
total_records = len(pre_sale_data)

# identify records with at least one missing sort_values - use .isnull().any(axis=1)  
missing_values_records = pre_sale_data[pre_sale_data.isnull().any(axis=1)]  # check for nulls in any column for each row
# count the number of records with at least one missing sort_values
missing_values_records_count = len(missing_values_records)

# calculate the percentage of missing_values_records
missing_values_records_pct = (missing_values_records_count / total_records) * 100

# handle missing values in 'region' & 'demographic_group' - fill nulls with 'Unknown' placeholder
pre_sale_data_cleaned = pre_sale_data.copy() 
pre_sale_data_cleaned['region'].fillna('Unknown', inplace=True)
pre_sale_data_cleaned['demographic_group'].fillna('Unknown', inplace=True)

# print results
print(f"Percentage of records with missing values: {missing_values_records_pct}")


"""
Q2: What percentage of records have missing values in at least one column?
Handle the missing values, so that we have a cleaned dataset to work with.
"""

# extract the month from 'pre_order_date'
# dt.to_period(freq) - freq refer https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-period-aliases
pre_sale_data_cleaned['pre_order_month'] = pre_sale_data_cleaned['pre_order_date'].dt.to_period('M')

# group data by region, demographic_group, pre_order_month then sum by pre_order_quantity
monthly_orders = (pre_sale_data_cleaned.groupby(['region', 'demographic_group', 'pre_order_month'])['pre_order_quantity']
  .sum().reset_index())
monthly_orders


"""
Q3: Predict the total pre-sales quantity for each region for September 2024.  
Assume that growth rate from August to September, is the same as the growth rate from July to August in each region.
"""

 # filter DataFrame for July'24 & Aug'24
july_aug_2024_sale = pre_sale_data_cleaned[(pre_sale_data_cleaned['pre_order_date'].dt.year==2024) 
  & (pre_sale_data_cleaned['pre_order_date'].dt.month.isin([7, 8]))]

# calculate total pre-sales for each region for July'24 & Aug'24
# unstack(level=0) - pivot the first level of hierarchical index from row to column 
# fill any nulls with 0
monthly_regional_sales = (july_aug_2024_sale.groupby([july_aug_2024_sale['pre_order_date'].dt.month, 'region'])['pre_order_quantity']
  .sum().unstack(level=0).fillna(0))

# calculate growth rate from July'24 to Aug'24 for each region - (aug-july)/july
growth_rate = (monthly_regional_sales[8] - monthly_regional_sales[7]) / monthly_regional_sales[7]
# if july sales=0, [np.inf, -np.inf] handle errors
growth_rate = growth_rate.replace([np.inf, -np.inf], np.nan).fillna(0)

# predict Sept'24 sales by using growth_rate to Aug'24, monthly_regional_sales[8]
sept_2024_sale_pred = monthly_regional_sales[8] * (1 + growth_rate)

# final DataFrame for Sept'24 prediction and rename sept_2024_sale_pred series columns
sales_pred_df = pd.DataFrame({'region': sept_2024_sale_pred.index, 'sept_pred_order_qty': sept_2024_sale_pred.values})

# round sept_pred_order_qty to whole number & int dtypes
sales_pred_df['sept_pred_order_qty'] = sales_pred_df['sept_pred_order_qty'].round(0).astype(int)
sales_pred_df
