#### Module to import the data and treat for duplicates and NAs ####
#### Author: Ricardo Santos ####


# Import libraries

import pandas as pd
import os

# Set current working directory

cwd = os.getcwd()

# Import data

building_data = pd.read_feather('site0.ft')

# Describe the dataset

def data_characterization(df):

    info = df.info()
    description = df.describe()

    return info, description


data_info, data_description = data_characterization(building_data)

# Identify duplicates

def data_duplicates(df):

    duplicates = sum(df.duplicated())
    if duplicates == 0:
        print('There are no duplicated entries')
    else:
        print('There are ' + str(duplicates) + ' duplicated entries')

    return 0


data_duplicates(building_data)

# Identify NAs

def data_nas(df):

    nas = sum(building_data.isna().sum())
    if nas == 0:
        print('There are no NAs')
    else:
        print('There are ' + str(nas) + ' duplicated entries')

    return 0


data_nas(building_data)

# Remove Nas


def drop_nas(df):

    df = df.dropna()

    return df


building_data = drop_nas(building_data)


# Save dataset to ft

def save_df_feather(df):

    df = df.reset_index()
    df.to_feather(cwd + '/' + 'UCF_Data_clean.ft')

    return 0


save_df_feather(building_data)









