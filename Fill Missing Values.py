
import pandas as pd

# Read Excel file
df = pd.read_excel('C:/Users/Administrator/Desktop/21.xlsx')

# Convert time strings to datetime objects
df['血糖时间'] = pd.to_datetime(df['血糖时间'])

# Create a new time series, generating time points at 5-minute intervals
start_time = pd.to_datetime('2023-04-17 00:00')
end_time = pd.to_datetime('2023-04-30 00:00')
new_time = pd.date_range(start=start_time, end=end_time, freq='5T')

# Set the time column as the index of the DataFrame
df.set_index('血糖时间', inplace=True)

# Generate a DataFrame with missing values using reindexing
df_interpolated = df.reindex(new_time)

# Compare based on rules and use original file values
for i, row in df_interpolated.iterrows():
    if i in df.index:
        df_interpolated.loc[i, '血糖'] = df.loc[i, '血糖']
    else:
        nearest_indices = df.index[(df.index >= i - pd.Timedelta(minutes=2)) & (df.index <= i + pd.Timedelta(minutes=2))]
        if len(nearest_indices) > 0:
            df_interpolated.loc[i, '血糖'] = df.loc[nearest_indices[-1], '血糖']

# Reset index and rename the time column
df_interpolated.reset_index(inplace=True)
df_interpolated.rename(columns={'index': '血糖时间'}, inplace=True)

# Fill missing values
for col in df_interpolated.columns[1:]:
    prev_val = None
    for i, val in enumerate(df_interpolated[col]):
        if pd.isnull(val):
            next_val = None
            j = i + 1
            while j < len(df_interpolated[col]) and pd.isnull(df_interpolated[col][j]):
                j += 1
            
            if j < len(df_interpolated[col]):
                next_val = df_interpolated[col][j]
            
            if prev_val is not None and next_val is not None:
                fill_value = (prev_val + next_val) / 2
                df_interpolated.at[i, col] = fill_value
        
        prev_val = df_interpolated[col][i]

# Round to one decimal place
df_interpolated = df_interpolated.round(1)

# Save processed data to a new Excel file
df_interpolated.to_excel('C:/Users/Administrator/Desktop/processed_data.xlsx', index=False)

# Print a message indicating successful saving
print("Processed data has been saved to: C:/Users/Administrator/Desktop/processed_data.xlsx")
