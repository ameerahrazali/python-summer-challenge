"""
Q1: Identify and remove any duplicate sales transactions from the dataset to ensure accurate analysis of seasonal patterns.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: ice_cream_sales_data

# identify and count duplicate rows 
duplicates_count = ice_cream_sales_data.duplicated().sum()

# remove duplicate rows from DataFrame
ice_cream_sales_cleaned = ice_cream_sales_data.drop_duplicates().copy()

# get final number of records after cleaned
final_records = len(ice_cream_sales_cleaned)

# print summary
print(f"Number of duplicate records found and removed: {duplicates_count}")
print(f"Final number of records after cleaning: {final_records}")


"""
Q2: Create a pivot table to summarize the total sales volume of ice cream products by month and temperature range.
Use the following temperature bins where each bin excludes the upper bound but includes the lower bound:
- Less than 60 degrees
- 60 to less than 70 degrees
- 70 to less than 80 degrees
- 80 to less than 90 degrees
- 90 to less than 100 degrees
- 100 degrees or more
"""

 # drop any rows where 'temperature' is NaN
ice_cream_sales_no_null = ice_cream_sales_cleaned.dropna(subset=['temperature']).copy()

# extract month from 'sale_date'
ice_cream_sales_no_null['sale_month'] = ice_cream_sales_no_null['sale_date'].dt.to_period('M')

# define 'temperature' bins and labels for categorization 
bins = [0, 60, 70, 80, 90, 100, float('inf')]
labels = ['<60', '60-69', '70-79', '80-89', '90-99', '100+']

# categorize 'temperature' into the defined bins then assign to new series
ice_cream_sales_no_null['temperature_range'] = pd.cut(ice_cream_sales_no_null['temperature'], bins=bins, labels=labels, 
                                                      right=False,   # This ensures the bins are [0,60), [60,70), etc.
                                                      include_lowest=True)   # if excluded any temperature=0 would fall outside bins then will be NaN

# create a pivot table to summarize total sales_volume
# index=month, columns=temperature_range, values=sales_volume
monthly_sales_summary = pd.pivot_table(ice_cream_sales_no_null, values='sales_volume', index='sale_month', columns='temperature_range', aggfunc='sum')
monthly_sales_summary


"""
Q3: Can you detect any outliers in the monthly sales volume using the Inter Quartile Range (IQR) method? 
A month is considered an outlier if falls below Q1 minus 1.5 times the IQR or above Q3 plus 1.5 times the IQR.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: ice_cream_sales_data
# Please print your final result or dataframe

 # calculate total sales_volume for each month
monthly_sales_volume = ice_cream_sales_cleaned.groupby(ice_cream_sales_cleaned['sale_date'].dt.to_period('M'))['sales_volume'].sum()

# calculate the IQR for monthly_sales_volume
q1 = monthly_sales_volume.quantile(0.25)
q3 = monthly_sales_volume.quantile(0.75)
iqr = q3 - q1

# define the upper and lower bound for outlier
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# identify the outliers
outliers = monthly_sales_volume[(monthly_sales_volume < lower_bound) | (monthly_sales_volume > upper_bound)]

# print the results
# .2f - format to 2 dp
print(f"Calculated Q1: {q1:.2f}")
print(f"Calculated Q3: {q3:.2f}")
print(f"Calculated IQR: {iqr:.2f}")
print(f"\nLower Outlier Bound: {lower_bound:.2f}")
print(f"Upper Outlier Bound: {upper_bound:.2f}")

print("\nOutlier Months Detected:")
print(outliers)
