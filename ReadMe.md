# Time series prediction 

## Goal 

This project aims at importing data from a file available in the Kaggle platform:

https://www.kaggle.com/teeyee314/ucf-building-meter-reading

<p>After importing the file, I will treat the data to remove duplicates and missing values.
I will assume that the outliers are part of the dataset, so they are benign to the dataset and not a problem. 
</p>
<p>
Having the data in a usable format, I will represent it on a dashboard. 
The top plot will have the total electrical consumption for each building. 
The bottom plot will have the chiller consumption for each building.
</p>

## Steps 

1. Treat the data
   1. Describe the dataset
   2. Remove duplicates
   3. Remove NAs
   

2. Visualize the data
   1. Plot total electricity consumption
   2. Plot chiller consumption
   3. Update graphs with building selection
3. Predict next year of building consumption by meter type (Electricity and chiller)