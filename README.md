## Movie Rating Data
We begin by cleaning the movie rating data, where we've identified numerical inconsistencies across the dataset. The number of entries varies with some datasets containing 79, 80, or 82 records. Additionally, we've noticed discrepancies in column names that actually represent the same data across various file despite their different labels. These might be due to the change of the IMBD website. 

### Findings
For detailed column information, please refer to Column Mapping.xlsx. Essentailly, using dataset with 82 file as based, the changes we have are:

#### 80 Columns
* Missing Rating Average IMDb staff (M_RATING_STAFF ) and Rating Votes IMDb staff (N_RATING_STAFF).
* Rating Average IMDb staff should be Rating Average Top 1000 voters(M_TOPUSER).
* Rating Average Top 1000 voters should be Rating Average US users (M_RATING_US).
* Rating Average US users should be Rating Average Non-US users (M_RATING_NUS).
* Rating Votes IMDb staff should be Rating Votes Top 1000 voters (N_TOPUSER).
* Rating Votes Top 1000 voters should be Rating Votes US users (N_US).
* Rating Votes US users should be Rating Votes Non-US users (N_NUS).

#### 79 Columns
Same changes as 80 but with additional column Rating Votes Females under 18 (N_F_U18) missing.

After the renaming all the columns, we scrape the date and time when the rating was scrape from the webpage on the data set file name. Next is to separate the time vary columns and the time invary columns. Then we consolidate all the data we have into one large data set, then keep the unique one for later use.


## Advertisement Data
First we have the data set contains information on the following:
* CATEGORY
* PRODUCT - Movie name, some are promotion video. 
* MEDIA - The way movie was advertise
* TOTAL DOLS - Total dollar spent on advertisement (sum of all week)
* WK ..... - Contains the money spend on advertisement for the week from 2016 August to 2020 April.

What we do next is to join another matching data set that contains PRODUCT and their IMBD_ID. Join the two dataset based on PRODUCT. Then we have the advertisement dataset with IMDB_ID. Some does not have ID because they are promotion video, they are not on IMDB. 

Then we transpose the week information (from wider dataset to longer dataset) for future analysis. 

















