import os
import pandas as pd

# Define the directory where your CSV files are located
csv_directory = '/Users/sammi/Desktop/Re_Column - 80'

# Define the directory on your desktop where you want to save the extracted files
desktop_directory = os.path.expanduser('/Users/sammi/Desktop/Time_Vary - 80')

# Define the columns you want to extract (without "New_" prefix)
columns_to_extract = [
    'DATE_SCRAPE', 'TIME_SCRAPE', 'CHAIN_URL', 'SOURCE_URL', 'DEMO_NON_US_RATING01', 'DEMO_NON_US_RATING02',
    'DEMO_NON_US_RATING03', 'DEMO_NON_US_RATING04', 'DEMO_NON_US_RATING05',
    'DEMO_NON_US_RATING06', 'DEMO_NON_US_RATING07', 'DEMO_NON_US_RATING08',
    'DEMO_NON_US_RATING09', 'DEMO_NON_US_RATING10', 'DEMO_US_RATING01',
    'DEMO_US_RATING02', 'DEMO_US_RATING03', 'DEMO_US_RATING04', 'DEMO_US_RATING05',
    'DEMO_US_RATING06', 'DEMO_US_RATING07', 'DEMO_US_RATING08', 'DEMO_US_RATING09',
    'DEMO_US_RATING10', 'RATING01', 'RATING02', 'RATING03', 'RATING04',
    'RATING05', 'RATING06', 'RATING07', 'RATING08', 'RATING09', 'RATING10',
    'M_RATING_A18', 'M_RATING_A30', 'M_RATING_A45', 'M_RATING_U18', 'M_RATING_F',
    'M_RATING_F_A18', 'M_RATING_F_A30', 'M_RATING_F_A45', 'M_RATING_F_U18',
    'M_RATING_TOPUSER', 'M_RATING_M', 'M_RATING_M_A18', 'M_RATING_M_A30', 'M_RATING_M_A45',
    'M_RATING_M_U18', 'M_RATING_US', 'M_RATING_NUS', 'N_A18', 'N_A30', 'N_A45',
    'N_U18', 'N_F', 'N_F_A18', 'N_F_A30', 'N_F_A45', 'N_F_U18', 'N_TOPUSER',
    'N_M', 'N_M_A18', 'N_M_A30', 'N_M_A45', 'N_M_U18', 'N_US', 'N_NUS'

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
        output_file = os.path.join(desktop_directory, 'extracted_' + filename)
        extract_and_save_columns(input_file, output_file, columns_to_extract)

print(f"Results exported")