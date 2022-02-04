import pandas as pd
import os

cwd = os.getcwd()

building_data = pd.read_feather('site0.ft')


def data_characterization(df):

    info = df.info()
    description = df.describe()

    return info, description


data_info, data_description = data_characterization(building_data)


def data_duplicates(df):

    duplicates = sum(df.duplicated())
    if duplicates == 0:
        print('There are no duplicated entries')
    else:
        print('There are ' + str(duplicates) + ' duplicated entries')

    return 0


data_duplicates(building_data)








