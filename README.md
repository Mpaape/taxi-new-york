# New York City Taxi Fare Prediction

Project to pratice some end to end pipelines in datascience.  You can find all data e instructions on https://www.kaggle.com/competitions/new-york-city-taxi-fare-prediction/data


### Motivation? why did i made a basic project ?
    
    Train some datascience solution patterns to speed up my productivity at all. The real world soluction problably will pass through a lot data processing to build a database and some conversations with business area to understand the real need of the project.


# Dataset Description

## File descriptions
* train.csv - Input features and target fare_amount values for the training set (about 55M rows).

* test.csv - Input features for the test set (about 10K rows). Your goal is to predict fare_amount for each row.

* sample_submission.csv - a sample submission file in the correct format (columns key and fare_amount). This file 'predicts' fare_amount to be $11.35 for all rows, which is the mean fare_amount from the training set.


## Data fields
* ID key - Unique string identifying each row in both the training and test sets. Comprised of pickup_datetime plus a unique integer, but this doesn't matter, it should just be used as a unique ID field.

* Required in your submission CSV. Not necessarily needed in the training set, but could be useful to simulate a 'submission file' while doing cross-validation within the training set.

## Features
* pickup_datetime - timestamp value indicating when the taxi ride started.
* pickup_longitude - float for longitude coordinate of where the taxi ride started.
* pickup_latitude - float for latitude coordinate of where the taxi ride started.
* dropoff_longitude - float for longitude coordinate of where the taxi ride ended.
* dropoff_latitude - float for latitude coordinate of where the taxi ride ended.
* passenger_count - integer indicating the number of passengers in the taxi ride.

## Target
* fare_amount - float dollar amount of the cost of the taxi ride. This value is only in the training set; this is what you are predicting in the test set and it is required in your submission CSV.

## get data

 > !kaggle competitions download -c  new-york-city-taxi-fare-prediction
## Repository Description
```
taxi-new-york/
| -- data/
| -- model/
| -- notebooks/
| -- reports/
| -- src/
```

