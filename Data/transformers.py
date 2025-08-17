import pandas as pd

# Define the data
data = {
    'user_id': [1, 1, 2, 2, 2, 3],
    'activity_date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-02', '2022-01-03'],
    'activity_type': ['login', 'view_item', 'login', 'view_item', 'purchase', 'login']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Convert the 'activity_date' column to datetime
df['activity_date'] = pd.to_datetime(df['activity_date'])

print(df)