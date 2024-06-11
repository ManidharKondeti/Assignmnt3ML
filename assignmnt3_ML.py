import pandas as pd

# 1: Read the CSV file
# reading the provided CSV file locally
# df = pd.read_csv('G:/My Files/UCM/Masters/Summer_2024/Machine Learning/Assignment3/data.csv')
# reading the provided CSV file after uploading the file to Github
df = pd.read_csv('https://raw.githubusercontent.com/ManidharKondeti/Assignmnt3ML/main/data.csv')

print(" CSV file read successfully:\n", df.head())

# 2: Show basic statistical description
description = df.describe()
print("\n Basic statistical description:\n", description)

# 3: Check for null values and replace with mean
# Check if the data has null values.
print('Are there any null values present in data: ', df.isnull().values.any())
# Replace the null values with the mean
df.fillna(df.mean(), inplace=True)
print('Are there any null values after using fillna: ', df.isnull().values.any())

# 4: Aggregate data using min, max, count, and mean
aggregated_data = df[['Calories', 'Pulse']].agg(['min', 'max', 'count', 'mean'])
print("\n Aggregated data:\n", aggregated_data)

# 5: Filter rows with calories values between 500 and 1000
filtered_df_1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print("\n Filtered DataFrame (calories between 500 and 1000):\n", filtered_df_1)

# 6: Filter rows with calories > 500 and pulse < 100
filtered_df_2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print("\n Filtered DataFrame (calories > 500 and pulse < 100):\n", filtered_df_2)

# 7: Create new dataframe with all columns except 'Max pulse'
df_modified = df[['Duration', 'Pulse', 'Calories']]
print("\n New DataFrame (df_modified) without 'Max pulse' column :\n", df_modified)

# 8: Delete 'Max pulse' column from main dataframe
res = df.drop(columns=['Maxpulse'], axis=1)
print("\n 'Max pulse' column removed from main DataFrame:\n", res)

# 9: Convert datatype of 'Calories' column to int
df['Calories'] = df['Calories'].astype(int)
print("\n Datatype of 'Calories' column converted to int:\n", df['Calories'])
