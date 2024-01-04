import pandas as pd
from datetime import datetime, timedelta
import re

# Read the Excel file
df = pd.read_excel("Date_conversion.xlsx")

# Function to convert various date formats to DD-mm-YYYY
def convert_to_dd_mm_yyyy(date_str):
    try:
        # Try to parse the date using the first format
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        try:
            # Try to parse the date using the second format
            match = re.match(r'(\w{3} \d{1,2}, \d{4} at \d{1,2}:\d{2} [APMapm]+) ([A-Za-z]+)', date_str)
            if match:
                dt_str, timezone = match.groups()
                dt = datetime.strptime(dt_str, "%b %d, %Y at %I:%M %p")
                # Adjust the time based on the IST timezone
                if timezone.upper() == 'IST':
                    dt += timedelta(hours=5, minutes=30)
            else:
                raise ValueError
        except ValueError:
            # If none of the formats match, return the original string
            return date_str
    # Convert the date to DD-mm-YYYY format
    return dt.strftime("%d-%m-%Y")

# Apply the conversion function to the "Date" column
df['Date'] = df['Date'].apply(convert_to_dd_mm_yyyy)

df.to_excel("output_excel_file.xlsx", index=False)
