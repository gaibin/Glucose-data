import pandas as pd

# Read data file
file_path = "C:/Users/Administrator/Desktop/1.csv"  # Please modify the actual file path
df = pd.read_csv(file_path)

# Merge date and time columns into a new column
df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['epoch'])

# Filter data before April 28th
start_date = pd.to_datetime('2023-04-28')
filtered_df = df[df['datetime'] < start_date]

# Arrange time column in 5-minute intervals, and other columns using summation
agg_dict = {
    'axis1': 'sum',
    'axis2': 'sum',
    'axis3': 'sum',
    'vm': 'sum',
    'steps': 'sum',
    'lux': 'sum',
    'inclinometer off': 'sum',
    'inclinometer standing': 'sum',
    'inclinometer sitting': 'sum',
    'inclinometer lying': 'sum',
    'kcals': 'sum',
    'MET rate': 'mean'
}

# Group data by time column and apply aggregation functions
grouped_df = filtered_df.groupby(pd.Grouper(key='datetime', freq='5Min')).agg(agg_dict)

# Reset index and keep date and time columns
grouped_df.reset_index(inplace=True)

# Output results
print(grouped_df)

# Save the result as a CSV file
output_file_path = "C:/Users/Administrator/Desktop/output.csv"  # Please modify the actual output path
grouped_df.to_csv(output_file_path, index=False)
