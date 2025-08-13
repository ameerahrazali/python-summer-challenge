# Q1: For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent? 
# This insight will help assess engagement in larger groups and support recommendations for group messaging features.

# for a group more than 50 in oct 2024
filtered_groups = dim_groups[(dim_groups['created_date'].dt.year == 2024) &
                           (dim_groups['created_date'].dt.month == 10) &
                           (dim_groups['participant_count'] > 50)]

# find average messages in the filtered group_id
avg_messages = filtered_groups['total_messages'].mean()

# print the result
print(f"The average number messages sent for filtered group is : {avg_messages}")


# Q2: What is the average number of participants in WhatsApp groups that were created in October 2024? 
# This number will indicate the typical group size and inform our group messaging feature considerations.

 # Filter for groups created in October 2024
oct_groups = dim_groups[(dim_groups['created_date'].dt.year == 2024) & (dim_groups['created_date'].dt.month == 10)]

# Find the average participant count
avg_participants = oct_groups['participant_count'].mean()

# Print the result
print(f"The average number of participants in groups created in October 2024 is: {avg_participants}")


# Q3: For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent?
# This insight will help assess engagement in larger groups and support recommendations for group messaging features.

# for a group more than 50 in oct 2024
filtered_groups = dim_groups[(dim_groups['created_date'].dt.year == 2024) &
                           (dim_groups['created_date'].dt.month == 10) &
                           (dim_groups['participant_count'] > 50)]

# find average messages in the filtered group_id
avg_messages = filtered_groups['total_messages'].mean()

# print the result
print(f"The average number messages sent for filtered group is : {avg_messages}")
