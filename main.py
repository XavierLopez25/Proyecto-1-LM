import pandas as pd
import re

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

# Initialize an empty list to hold each row's data
data_rows = []

# Read the file line by line
with open("BL-Flickr-Images-Book.csv", "r", encoding='utf-8') as file:
    headers = next(file).strip().split(',')  # Extract headers separately
    for line in file:
        # Split the line using regex to handle commas within quotes
        fields = re.split(regex_pattern, line.strip())
        # Clean up any double quotes encapsulating fields
        fields = [field.strip('"') for field in fields]
        data_rows.append(fields)

# Create a DataFrame from the list of rows
df_from_regex = pd.DataFrame(data_rows, columns=headers)

# Convert the DataFrame to a string format with line breaks between rows
df_string = df_from_regex.head(100).to_string()

# Write the string to a text file
with open("output.txt", "w", encoding='utf-8') as text_file:
    text_file.write(df_string)

print("Data written to output.txt successfully!")
