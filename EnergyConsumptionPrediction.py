#### Module to train the LSTM and predict future data ####
#### Author: Ricardo Santos ####

# Import libraries

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Dense
from sklearn.metrics import mean_squared_error, median_absolute_error

# Import the data


def data_import(path):

    cwd = os.getcwd()
    data = pd.read_feather(os.path.join(cwd, path))

    return data


df_ucf = data_import('UCF_Data_clean.ft')


def select_meter_and_building(data, meter, building):

    data = data[(data['meter'] == 0)
                & (data['building_id'] == 0)]

    return data


df_ucf = select_meter_and_building(df_ucf, 0, 0)

# Define training data for building 0 and meter 0 (electricity)

train_data, test_data = train_test_split(df_ucf, test_size=0.2, random_state=2)

# Scale the data


def scale_data(train_set, test_set):

    scaler = StandardScaler()
    scaler = scaler.fit(train_set[['meter_reading']])

    train_set['meter_reading'] = scaler.transform(train_set[['meter_reading']])
    test_set['meter_reading'] = scaler.transform(test_set[['meter_reading']])

    return train_set, test_set


train_data, test_data = scale_data(train_data, test_data)
