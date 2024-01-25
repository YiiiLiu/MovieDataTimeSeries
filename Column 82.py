import os
import re
import pandas as pd

# Function to extract date from a file name
def extract_date(file_name):
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', file_name)
    return date_match.group(0) if date_match else ""

# Function to extract time from a file name
def extract_time(file_name):
    parts = re.split(r'[\s-]', file_name)
    for part in parts:
        if re.match(r'\d{2}.\d{2}.\d{2}', part):
            return part.replace('.', ':')
    return None

# Function to add date and time columns to files in a directory
def add_date_and_time_columns(directory, output_folder_name):
    desktop_path = os.path.join(os.path.expanduser('/Users/sammi'), 'Desktop', output_folder_name)
    os.makedirs(desktop_path, exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]

                scraped_date = extract_date(file_name)
                scraped_time = extract_time(file_name)

                df = pd.read_csv(file_path)
                df['DATE_SCRAPE'] = scraped_date
                df['TIME_SCRAPE'] = scraped_time

                output_file_path = os.path.join(desktop_path, f"{file_name}.csv")
                df.to_csv(output_file_path, index=False)

# Function to rename columns in a CSV file and save it
def rename_and_save_csv(input_file, output_file, column_mapping):
    df = pd.read_csv(input_file)
    df.rename(columns=column_mapping, inplace=True)
    df.to_csv(output_file, index=False)

# Function to extract specified columns and save to a new CSV file
def extract_and_save_columns(input_file, output_file, columns_to_extract):
    df = pd.read_csv(input_file)
    extracted_df = df[columns_to_extract]
    extracted_df.to_csv(output_file, index=False)

# Column mapping dictionary
column_mapping = {
    '.Chain URL' : 'CHAIN_URL',
    '.Source URL': 'SOURCE_URL',
    'Demo Non-US users - Rating 01': 'DEMO_NON_US_RATING01',
    'Demo Non-US users - Rating 02': 'DEMO_NON_US_RATING02',
    'Demo Non-US users - Rating 03': 'DEMO_NON_US_RATING03',
    'Demo Non-US users - Rating 04': 'DEMO_NON_US_RATING04',
    'Demo Non-US users - Rating 05': 'DEMO_NON_US_RATING05',
    'Demo Non-US users - Rating 06': 'DEMO_NON_US_RATING06',
    'Demo Non-US users - Rating 07': 'DEMO_NON_US_RATING07',
    'Demo Non-US users - Rating 08': 'DEMO_NON_US_RATING08',
    'Demo Non-US users - Rating 09': 'DEMO_NON_US_RATING09',
    'Demo Non-US users - Rating 10': 'DEMO_NON_US_RATING10',
    'Demo US users - Rating 01': 'DEMO_US_RATING01',
    'Demo US users - Rating 02': 'DEMO_US_RATING02',
    'Demo US users - Rating 03': 'DEMO_US_RATING03',
    'Demo US users - Rating 04': 'DEMO_US_RATING04',
    'Demo US users - Rating 05': 'DEMO_US_RATING05',
    'Demo US users - Rating 06': 'DEMO_US_RATING06',
    'Demo US users - Rating 07': 'DEMO_US_RATING07',
    'Demo US users - Rating 08': 'DEMO_US_RATING08',
    'Demo US users - Rating 09': 'DEMO_US_RATING09',
    'Demo US users - Rating 10': 'DEMO_US_RATING10',
    'Rating 01': 'RATING01',
    'Rating 02': 'RATING02',
    'Rating 03': 'RATING03',
    'Rating 04': 'RATING04',
    'Rating 05': 'RATING05',
    'Rating 06': 'RATING06',
    'Rating 07': 'RATING07',
    'Rating 08': 'RATING08',
    'Rating 09': 'RATING09',
    'Rating 10': 'RATING10',
    'Rating Average Aged 18-29': 'M_RATING_A18',
    'Rating Average Aged 30-44': 'M_RATING_A30',
    'Rating Average Aged 45+': 'M_RATING_A45',
    'Rating Average Aged under 18': 'M_RATING_U18',
    'Rating Average Females': 'M_RATING_F',
    'Rating Average Females Aged 18-29': 'M_RATING_F_A18',
    'Rating Average Females Aged 30-44': 'M_RATING_F_A30',
    'Rating Average Females Aged 45+': 'M_RATING_F_A45',
    'Rating Average Females under 18': 'M_RATING_F_U18',
    'Rating Average IMDb staff': 'M_RATING_STAFF',
    'Rating Average Males': 'M_RATING_M',
    'Rating Average Males Aged 18-29': 'M_RATING_M_A18',
    'Rating Average Males Aged 30-44': 'M_RATING_M_A30',
    'Rating Average Males Aged 45+': 'M_RATING_M_A45',
    'Rating Average Males under 18': 'M_RATING_M_U18',
    'Rating Average Non-US users' : 'M_RATING_NUS',
    'Rating Average Top 1000 voters': 'M_TOPUSER',
    'Rating Average US users': 'M_RATING_US',
    'Rating Votes Aged 18-29': 'N_A18',
    'Rating Votes Aged 30-44': 'N_A30',
    'Rating Votes Aged 45+': 'N_A45',
    'Rating Votes Aged under 18': 'N_U18',
    'Rating Votes Females': 'N_F',
    'Rating Votes Females Aged 18-29': 'N_F_A18',
    'Rating Votes Females Aged 30-44': 'N_F_A30',
    'Rating Votes Females Aged 45+': 'N_F_A45',
    'Rating Votes Females under 18': 'N_F_U18',
    'Rating Votes IMDb staff': 'N_RATING_STAFF',
    'Rating Votes Males': 'N_M',
    'Rating Votes Males Aged 18-29': 'N_M_A18',
    'Rating Votes Males Aged 30-44': 'N_M_A30',
    'Rating Votes Males Aged 45+': 'N_M_A45',
    'Rating Votes Males under 18': 'N_M_U18',
    'Rating Votes Non-US users' : "N_NUS",
    'Rating Votes Top 1000 voters': 'N_TOPUSER',
    'Rating Votes US users': 'N_US',
    'TT ID': 'IMDB_ID',
    'TT ID (_url)': 'MOVIE_URL',
    'age rating (_image - alt)': 'MPAA_TXT',
    'age rating (_image - src)': 'MPAA_IMG',
    'age rating (_image - title)': 'MPAA',
    'description': 'ABSTRACT',
    'director': 'DIRECTOR',
    'duration': 'RUNTIME',
    'genre': 'GENRE_1ST',
    'metascore': 'METASCORE',
    'title': 'TITLE',
    'title (_url)': 'TITLE_URL',
    'trailer URL': 'TRAILER_W',
    'trailer URL (_url)': 'TRAILER_URL',
    'DATE_SCRAPE' : 'DATE_SCRAPE',
    'TIME_SCRAPE' : 'TIME_SCRAPE'
}

columns_to_extract = [
    'IMDB_ID', 'MOVIE_URL', 'MPAA_TXT', 'MPAA_IMG', 'MPAA', 'ABSTRACT',
    'DIRECTOR', 'RUNTIME', 'GENRE_1ST', 'METASCORE', 'TITLE', 'TITLE_URL',
    'TRAILER_W', 'TRAILER_URL'
]


# Define directories
original_csv_directory = '/Users/sammi/Desktop/82_columns'
final_output_directory = os.path.expanduser('/Users/sammi/Desktop/TimeInvary')

# Ensure the output directory exists
os.makedirs(final_output_directory, exist_ok=True)

# Process the CSV files
for filename in os.listdir(original_csv_directory):
    if filename.endswith('.csv'):
        # Construct the full path to the original file
        input_file = os.path.join(original_csv_directory, filename)
        output_file = os.path.join(final_output_directory, filename)

        # Read the CSV file
        df = pd.read_csv(input_file)

        # Extract date and time from filename and add as columns
        scraped_date = extract_date(filename)
        scraped_time = extract_time(filename)
        df['DATE_SCRAPE'] = scraped_date
        df['TIME_SCRAPE'] = scraped_time

        # Rename columns based on the provided mapping
        df.rename(columns=column_mapping, inplace=True)

        # Extract specific columns
        if columns_to_extract:
            df = df[columns_to_extract]

        # Save the final DataFrame to a CSV file
        df.to_csv(output_file, index=False)

print(f"Results exported")