"""
Q1: What is the average driver earnings per completed UberPool ride with more than 
two riders between July 1st and September 30th, 2024? This analysis will help isolate trips 
that meet specific rider thresholds to understand their impact on driver earnings.
"""

# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_trips

# define the start and end dates for Q3 2024
start_date = '2024-07-01'
end_date = '2024-09-30'

# filter the DataFrame as ride_type='UberPool' & rider_count>2 & trip_date is in Q3'24
filtered_trips = fct_trips[(fct_trips['ride_type'] == 'UberPool') 
  & (fct_trips['rider_count'] > 2)
  & (fct_trips['trip_date'] >= start_date) 
  & (fct_trips['trip_date'] <= end_date)].copy()

# calculate avg of total_earnings from filtered_trips
avg_earnings = filtered_trips['total_earnings'].mean()

# print result
print(f"Average driver earnings per UberPool ride with more than two riders: ${avg_earnings:.2f}")


"""
Q2: For completed UberPool rides between July 1st and September 30th, 2024, derive a new column 
calculating earnings per mile (total_earnings divided by total_distance) and then compute the average earnings per mile
for rides with more than two riders. This calculation will reveal efficiency metrics for driver compensation.
"""

# define the start and end dates for Q3 2024
start_date = '2024-07-01'
end_date = '2024-09-30'

# filter the DataFrame as ride_type='UberPool' & trip_date is in Q3'24
uberpool_trips = fct_trips[(fct_trips['ride_type'] == 'UberPool') 
  & (fct_trips['trip_date'] >= start_date) 
  & (fct_trips['trip_date'] <= end_date)].copy()

# calculate earnings per mile & use epsilon to avoid division by 0
epsilon = 1e-9
uberpool_trips['earnings_per_mile'] = uberpool_trips['total_earnings'] /(uberpool_trips['total_distance'] + epsilon)

# filter for rides where rider_count > 2
high_rider_trips = uberpool_trips[uberpool_trips['rider_count'] > 2].copy()

# compute avg of earnings_per_mile for high_rider_trips
avg_earnings_per_mile = high_rider_trips['earnings_per_mile'].mean()

# print result
print(f"Average earnings per mile for UberPool rides with more than two riders: ${avg_earnings_per_mile:.2f}")


"""
Q3:  Identify the combination of rider count and total distance that results in the 
highest average driver earnings per UberPool ride between July 1st and September 30th, 2024.
This analysis directly recommends optimal trip combination strategies to maximize driver earnings.
"""

# define the start and end dates for Q3 2024
start_date = '2024-07-01'
end_date = '2024-09-30'

# filter the DataFrame as ride_type='UberPool' & trip_date is in Q3'24
uberpool_trips = fct_trips[(fct_trips['ride_type'] == 'UberPool') 
  & (fct_trips['trip_date'] >= start_date) 
  & (fct_trips['trip_date'] <= end_date)].copy()

# group uberpool_trips by 'rider_count' and 'total_distance' then compute avg 'total_earnings'
optimal_combo = uberpool_trips.groupby(['rider_count', 'total_distance'])['total_earnings'].mean().reset_index()

# sort optimal_combo in descending order
sorted_optimal_combo = optimal_combo.sort_values(by='total_earnings', ascending=False)

# get top row as highest-earning
highest_earning_combo = sorted_optimal_combo.iloc[0]

# print result
print(f"Combination of rider count and total distance with the highest average driver earnings:")
print(highest_earning_combo)
