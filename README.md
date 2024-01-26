## Movie Rating Data
The data were scraped from the IMBD website hourly. We begin by cleaning the movie rating data, where we've identified numerical inconsistencies across the dataset. The number of entries varies with some datasets containing 60, 79, 80, or 82 records. Additionally, we've noticed discrepancies in column names that actually represent the same data across various file despite their different labels. These might be due to the change of the IMBD website. We have total of 23717 datasets. 82 has 3928, 80 has 19500, 79 has 287, 60 has 2.

### Findings on Column Inconsistency
For detailed column information, please refer to Column Mapping.xlsx. Essentailly, using dataset with 82 file as a base, the changes we have are:

#### 80 Columns
* Missing Rating Average IMDb staff (M_RATING_STAFF ) and Rating Votes IMDb staff (N_RATING_STAFF).
* Rating Average IMDb staff should be Rating Average Top 1000 voters(M_TOPUSER).
* Rating Average Top 1000 voters should be Rating Average US users (M_RATING_US).
* Rating Average US users should be Rating Average Non-US users (M_RATING_NUS).
* Rating Votes IMDb staff should be Rating Votes Top 1000 voters (N_TOPUSER).
* Rating Votes Top 1000 voters should be Rating Votes US users (N_US).
* Rating Votes US users should be Rating Votes Non-US users (N_NUS).

Dataset: From 2018-05-25 05.00.00 to 2020-09-17 19.42.23. 

#### 79 Columns
* Same changes as 80 but with additional column Rating Votes Females under 18 (N_F_U18) missing.

Dataset: 2020-05-22 18.00.00 and from 2020-06-01 00.00.00 to 2020-06-12 21.00.00.

#### 60 Columns
* Missing all the Demo columns.
* Rating Votes IMDb staff and Rating Votes Males under 18 are also missing.

Datasets: 2018-04-02 00.00.00 and 2018-07-29 19.00.00. A note about this is that they are all the days with few data being scraped. 2018-04-02 we only have one, 2018-07-29 we only have three. 

### Next Step
After identifying these inconsistencies, we proceeded to extract the date and time of when the ratings were scraped, using the dataset filenames as our source. Then, we renamed all the columns for clarity and separate them into two categories: 'time vary' and 'time invary' columns. Time vary columns contain ratings that changes across the dataset. In contrast, time invary columns has data that remain consistent throughout the dataset, meaning that for the same movie in different datasets, this information stays the same, like link or title. Our goal is to drop the duplicate rows while preserving unique entries identified by their IMDB_ID and TITLE for in-depth future analysis. 

## Advertisement Data
First we have the data set contains information on the following:
* CATEGORY
* PRODUCT - Movie name, some are promotion video. 
* MEDIA - The way movie was advertise
* TOTAL DOLS - Total dollar spent on advertisement (sum of all week)
* WK ..... - Contains the money spend on advertisement for the week from 2016 August to 2020 April.

What we do next is to join another matching data set that contains PRODUCT and their IMBD_ID. Join the two dataset based on PRODUCT. Then we have the advertisement dataset with IMDB_ID. Some does not have ID because they are promotion video, they are not on IMDB. 

Then we transpose the week information (from wider dataset to longer dataset) for future analysis. 

















