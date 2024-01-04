import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import re
import os

def convert_to_dd_mm_yyyy(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        try:
            match = re.match(r'(\w{3} \d{1,2}, \d{4} at \d{1,2}:\d{2} [APMapm]+) ([A-Za-z]+)', date_str)
            if match:
                dt_str, timezone = match.groups()
                dt = datetime.strptime(dt_str, "%b %d, %Y at %I:%M %p")
                if timezone.upper() == 'IST':
                    dt += timedelta(hours=5, minutes=30)
            else:
                raise ValueError
        except ValueError:
            return date_str
    return dt.strftime("%d-%m-%Y")

def convert_dates(df):
    df['Date'] = df['Date'].apply(convert_to_dd_mm_yyyy)
    return df

def main():
    st.title("Date Conversion App")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)

        st.subheader("Original DataFrame:")
        st.write(df)

        converted_df = convert_dates(df)

        st.subheader("Modified DataFrame:")
        st.write(converted_df)

        # Create the "downloads" directory if it doesn't exist
        os.makedirs("downloads", exist_ok=True)

        # Save the modified DataFrame to a new Excel file in the "downloads" folder
        output_file_path = "downloads/output_excel_file.xlsx"
        converted_df.to_excel(output_file_path, index=False)

        st.success("Conversion completed.")

        # Provide a download button for the modified file
        st.download_button("Download Modified File", output_file_path)

if __name__ == "__main__":
    main()
