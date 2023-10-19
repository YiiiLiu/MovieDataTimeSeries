import os
import re
import pandas as pd

##add_date_and_time_columns('/Users/sammi/Desktop/20181204', '/Users/sammi/Desktop/20181204 - Result')

def extract_date(file_name):
    # Use regular expression to capture date in the format YYYY-MM-DD
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', file_name)

    scraped_date = date_match.group(0) if date_match else ""

    return scraped_date

def extract_time(file_name):
    # Split the file name by spaces and hyphens
    parts = re.split(r'[\s-]', file_name)

    # Find the time component
    scraped_time = None

    for part in parts:
        if re.match(r'\d{2}.\d{2}.\d{2}', part):
            scraped_time = part.replace('.', ':')

    return scraped_time

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

                # Add the extracted date and time as new columns
                df['DATE_SCRAPE'] = scraped_date
                df['TIME_SCRAPE'] = scraped_time

                # Specify the output file path in the folder on the desktop
                output_file_path = os.path.join(desktop_path, f"{file_name}_with_datetime.csv")

                # Save the updated CSV file with the new columns
                df.to_csv(output_file_path, index=False)

# Call the function with the directory path and the desired output folder name
add_date_and_time_columns('/Users/sammi/Desktop/DataQualityFiles - 82', '/Users/sammi/Desktop/Result - 82')

print(f"Results exported")