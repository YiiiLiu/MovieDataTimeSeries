# MovieDataTimeSeries
This part of the document is aim to provide detail code and findings we have during the analysis process.

## Movie Rating Data
We begin by cleaning the movie rating data, where we've identified numerical inconsistencies across the dataset. The number of entries varies with some datasets containing 79, 80, or 82 records. Additionally, we've noticed discrepancies in column names that actually represent the same data across various file despite their different labels. These might be due to the change of the IMBD website. 

#### Findings
For all columns information, please refer to Column Mapping.py. Using dataset with 82 file as based, essentailly the changes we have are:

