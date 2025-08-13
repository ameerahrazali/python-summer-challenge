# Q1: For the product categories identified in the previous question, what is the percentage difference between their CTR and the overall average CTR for October 2024?
# This analysis will quantify the performance gap to recommend specific categories for targeted advertising optimization.
# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_ad_performance, dim_product
# Please print your final result or dataframe

 # merge the two dfs
df = pd.merge(fct_ad_performance, dim_product, on = 'product_id', how = 'inner')

# filter for records in Oct 2024 
oct_ads = df[(df['recorded_date'].dt.year == 2024) & 
              (df['recorded_date'].dt.month == 10)]

# calculate the CTR for each ad
oct_ads['ctr_individual'] = oct_ads['clicks'] / oct_ads['impressions']

# calculate the overall avg ctr for oct 2024
overall_avg_ctr = oct_ads['ctr_individual'].mean()

# group by product category and compute average of individual CTRs oct 24
average_ctr_by_category =  oct_ads.groupby('product_category')['ctr_individual'].mean().reset_index()

# filter for categories with ctr > overall avg
high_performing_categories = average_ctr_by_category[average_ctr_by_category['ctr_individual'] > overall_avg_ctr]

# calculate the % difference for high performed categories
high_performing_categories['pct_difference'] = ((high_performing_categories['ctr_individual'] - overall_avg_ctr) / overall_avg_ctr) * 100

# Print the final result
print(high_performing_categories[['product_category', 'pct_difference']])


# Q2: Which product categories have a CTR greater than the aggregated overall average CTR for sponsored product ads during October 2024?
# This analysis will identify high-performing categories for further optimization.
# For this question, we want to calculate CTR for each ad, then get the average across ads by product category & overall.

# merge the two dfs
df = pd.merge(fct_ad_performance, dim_product, on = 'product_id', how = 'inner')

# filter for records in Oct 2024 
oct_ads = df[(df['recorded_date'].dt.year == 2024) & 
              (df['recorded_date'].dt.month == 10)]

# calculate the CTR for each ad
oct_ads['ctr_individual'] = oct_ads['clicks'] / oct_ads['impressions']

#calculate overall average ctr for oct 2024
overall_avg_ctr =  oct_ads['ctr_individual'].mean()

# group by product category and compute average of individual CTRs
category_avg_ctr =  oct_ads.groupby('product_category')['ctr_individual'].mean().reset_index()

# filter for CTR > overall average
high_performing_categories = category_avg_ctr[category_avg_ctr['ctr_individual'] > overall_avg_ctr]

# Print the final result
print(high_performing_categories)


# Q3: For the product categories identified in the previous question, what is the percentage difference between their CTR and the overall average CTR for October 2024?
# This analysis will quantify the performance gap to recommend specific categories for targeted advertising optimization.

 # merge the two dfs
df = pd.merge(fct_ad_performance, dim_product, on = 'product_id', how = 'inner')

# filter for records in Oct 2024 
oct_ads = df[(df['recorded_date'].dt.year == 2024) & 
              (df['recorded_date'].dt.month == 10)]

# calculate the CTR for each ad
oct_ads['ctr_individual'] = oct_ads['clicks'] / oct_ads['impressions']

# calculate the overall avg ctr for oct 2024
overall_avg_ctr = oct_ads['ctr_individual'].mean()

# group by product category and compute average of individual CTRs oct 24
average_ctr_by_category =  oct_ads.groupby('product_category')['ctr_individual'].mean().reset_index()

# filter for categories with ctr > overall avg
high_performing_categories = average_ctr_by_category[average_ctr_by_category['ctr_individual'] > overall_avg_ctr]

# calculate the % difference for high performed categories
high_performing_categories['pct_difference'] = ((high_performing_categories['ctr_individual'] - overall_avg_ctr) / overall_avg_ctr) * 100

# Print the final result
print(high_performing_categories[['product_category', 'pct_difference']])
