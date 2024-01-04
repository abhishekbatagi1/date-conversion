import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
file_path = 'Date_conversion.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Convert the 'Date' column to datetime if it's not already in that format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove timezone information
df['Date'] = df['Date'].dt.tz_localize(None)

# Create a new column 'Formatted_Date' with the dates in YYYY-MM-DD format
df['Formatted_Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Save the DataFrame with formatted dates to a new Excel file
output_file_path = 'Formatted.xlsx'
df.to_excel(output_file_path, index=False)

print(f"The formatted dates have been saved to {output_file_path}")
