import pandas as pd
from dateutil import parser

# Creating a DataFrame with the provided date data
date_data = [
    "2024-01-06T12:05:20+0530",
    "2024-01-01T02:35:08+0530",
    "2024-06-12T00:55:18+0530",
    "Jan 2, 2024 at 11:20 AM IST",
    "2024-01-01T14:35:19+0530",
    "2024-01-10T14:10:23+0530",
    "2024-01-01T20:05:21+0530",
    "2024-01-01T12:00:04+0530",
    "2024-01-01T23:55:27+0530",
    "Jan 2, 2024 at 10:40 AM IST",
    "2024-01-06T22:00:15+0530",
    "2024-01-01T20:25:40+0530",
    "2024-01-07T11:00:39+0530",
    "2024-01-06T17:30:02+0530",
    "2024-01-01T17:30:58+0530"
]

df = pd.DataFrame({'Date': date_data})

# Convert the 'Date' column to datetime with custom timezone handling
df['Date'] = df['Date'].apply(lambda x: parser.parse(x, tzinfos={'IST': 330}) if not pd.isnull(x) else x)

# Check if 'Date' column is already in datetime format
if not pd.api.types.is_datetime64_any_dtype(df['Date']):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract the dates in YYYY/MM/DD format
df['Formatted_Date'] = df['Date'].dt.strftime('%Y/%m/%d')

# Print the results
print(df[['Date', 'Formatted_Date']])
