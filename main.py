import pandas as pd
import re
import numpy as np
import csv

# Regex pattern to split on commas that are not enclosed by quotes
# Explanation:
# r',             # Matches a comma
# (?=             # Start of a positive lookahead assertion
#    (?:          # Start of a non-capturing group
#       [^"]*"    # Match any number of non-quote characters followed by a quote
#       [^"]*"    # Match another set of any number of non-quote characters followed by a quote
#    )*           # End of the non-capturing group, repeated any number of times
#    [^"]*$       # Match any number of non-quote characters until the end of the line
# )'              # End of the lookahead assertion
regex_pattern = r',(?=(?:[^"]*"[^"]*")*[^"]*$)'

# Pattern that matches headers
header_pattern = r'[^,]+'

# Initialize an empty list to hold each row's data
data_rows = []

# Read the file line by line
with open("BL-Flickr-Images-Book.csv", "r", encoding='utf-8') as file:
    headers = re.findall(header_pattern, next(file).strip())  # Extract headers separately

    for line in file:
        # Split the line using regex to handle commas within quotes
        fields = re.split(regex_pattern, line.strip())
        # Remove enclosing double quotes if present and handle escaped quotes
        fields = [field[1:-1].replace('""', '"') if field.startswith('"') and field.endswith('"') else field for field in fields]
        data_rows.append(fields)

# Create a DataFrame from the list of rows
df_from_regex = pd.DataFrame(data_rows, columns=headers)

# Load the DataFrame using pandas' read_csv function with specific handling for quotes
df_from_read_csv = pd.read_csv("BL-Flickr-Images-Book.csv", dtype=str, quotechar='"', escapechar='\\', quoting=csv.QUOTE_ALL, on_bad_lines='skip')

# Function to check DataFrame equality with detailed feedback
def compare_dataframes(df1, df2):
    if df1.shape != df2.shape:
        print(f"Different shapes: df_from_regex: {df1.shape}, df_from_read_csv: {df2.shape}")
    elif not df1.columns.equals(df2.columns):
        print("Different columns:")
        print(f"df_from_regex columns: {df1.columns.tolist()}")
        print(f"df_from_read_csv columns: {df2.columns.tolist()}")
    else:
        # Replace NaN with empty strings for comparison
        df1 = df1.replace({np.nan: ""})
        df2 = df2.replace({np.nan: ""})
        
        # Check for differences in data
        differences = df1.ne(df2)
        if differences.any().any():
            print("Differences found in data:")
            diff_rows, diff_cols = differences.to_numpy().nonzero()
            for row, col in zip(diff_rows, diff_cols):
                col_name = df1.columns[col]
                print(f"Row {row}, Column '{col_name}':")
                print(f"  df_from_regex: '{df1.iloc[row, col]}'")
                print(f"  df_from_read_csv: '{df2.iloc[row, col]}'")
        else:
            print("\nBoth DataFrames are equal.\n\n")

# Compare both DataFrames
compare_dataframes(df_from_regex, df_from_read_csv)

# Print the number of columns and rows for df_from_regex
print("df_from_regex:")
print(f"Number of columns: {len(df_from_regex.columns)}")
print(f"Number of rows: {len(df_from_regex)}")

# Print the number of columns and rows for df_from_read_csv
print("\ndf_from_read_csv:")
print(f"Number of columns: {len(df_from_read_csv.columns)}")
print(f"Number of rows: {len(df_from_read_csv)}")

# Convert the DataFrame to a string format with line breaks between rows
df_string = df_from_regex.to_string()

# Write the string to a text file
with open("output.txt", "w", encoding='utf-8') as text_file:
    text_file.write(df_string)

print("\nData written to output.txt successfully!\n")
