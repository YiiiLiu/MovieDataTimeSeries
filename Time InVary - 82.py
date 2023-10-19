import os
import pandas as pd

# Define the directory where your CSV files are located
csv_directory = '/Users/sammi/Desktop/Re_Column - 82'

# Define the directory on your desktop where you want to save the extracted files
desktop_directory = os.path.expanduser('/Users/sammi/Desktop/Time_InVary - 82')

# Define the columns you want to extract (without "New_" prefix)
columns_to_extract = [
    'IMDB_ID', 'MOVIE_URL', 'MPAA_TXT', 'MPAA_IMG', 'MPAA', 'ABSTRACT',
    'DIRECTOR', 'RUNTIME', 'GENRE_1ST', 'METASCORE', 'TITLE', 'TITLE_URL',
    'TRAILER_W', 'TRAILER_URL'
]


# Function to extract specified columns and save to a new CSV file
def extract_and_save_columns(input_file, output_file, columns_to_extract):
    df = pd.read_csv(input_file)
    extracted_df = df[columns_to_extract]
    extracted_df.to_csv(output_file, index=False)

# Loop through the CSV files in the directory and extract specified columns
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        input_file = os.path.join(csv_directory, filename)
        output_file = os.path.join(desktop_directory, 'extracted_InVary_' + filename)
        extract_and_save_columns(input_file, output_file, columns_to_extract)

print(f"Results exported")