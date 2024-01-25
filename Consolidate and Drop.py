import os
import pandas as pd

def stack_csv_files(folder_path):
    all_data = []

    # Iterate through each subfolder
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(subdir, file)
                df = pd.read_csv(file_path)
                all_data.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df

# Replace 'your_main_folder_path' with the path to your main folder
folder_path = '/Users/sammi/Desktop/TimeInvary'
combined_df = stack_csv_files(folder_path)

#1270
drop_df = combined_df.drop_duplicates(subset=['IMDB_ID', 'TITLE'], keep='first')

#1097
#drop_df = combined_df.drop_duplicates(subset=['IMDB_ID'], keep='first')


output_file_path = '/Users/sammi/Desktop/IMBD_ID_Invary_unique.csv'
drop_df.to_csv(output_file_path, index=False)


print(drop_df)
