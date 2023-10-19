import os
import pandas as pd

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

# Directory where your CSV files are located
csv_directory = '/Users/sammi/Desktop/Result - 82'

# Directory where you want to save the modified files on your desktop
desktop_directory = os.path.expanduser('/Users/sammi/Desktop/Re_Column - 82')

# Function to rename columns in a CSV file and save it
def rename_and_save_csv(input_file, output_file, column_mapping):
    df = pd.read_csv(input_file)
    df.rename(columns=column_mapping, inplace=True)
    df.to_csv(output_file, index=False)

# Loop through the CSV files in the directory and rename columns
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        input_file = os.path.join(csv_directory, filename)
        output_file = os.path.join(desktop_directory, 'renamed_' + filename)
        rename_and_save_csv(input_file, output_file, column_mapping)


print(f"Results exported")