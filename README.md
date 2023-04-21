
# SurfForecast

This program analyzes the wave data stored in the "waves.txt" file. It preprocesses the data, extracts features, and trains several machine learning models to predict whether a given wave is small, medium, or large. The models used in this program include a decision tree, k-nearest neighbors, naive Bayes, and a voting classifier that combines the predictions of the other three models.

The program starts by reading the wave data file into a pandas dataframe and removing any rows that have a wave height of 99.0, which indicates bad data. It then extracts several features from the data, including wave height, month, day, DPD (Dominant Period), APD (Average Period), MWD (Mean Wave Direction), and WTMP (Water Temperature). It also normalizes these features using the MinMaxScaler.

Next, the program splits the data into training and testing sets, with 80% of the data used for training and 20% for testing. It then trains four different models: a decision tree, k-nearest neighbors, naive Bayes, and a voting classifier that combines the predictions of the other three models. The program also uses cross-validation to evaluate the performance of each model.

Finally, the program outputs the mean cross-validation scores for each model, indicating how well each model performs at predicting whether a given wave is small, medium, or large. The decision tree and voting classifier models tend to perform the best, with mean cross-validation scores of around 0.70-0.76. The k-nearest neighbors model performs slightly worse, with a mean cross-validation score of around 0.60. The naive Bayes model performs the worst, with a mean cross-validation score of around 0.60.


This is an ongoing project. I eventually want the model to tell you how clean the waves are going to be. Ex.) "The waves today given x y and z are classified as fair with a height of 2-3ft." The conditions will be based off of surflines ranking for waves, like poor,fair,good and up.

# Purpose of Creating this
My reasons for creating this is to build an application that is free to use for surfers local to Virginia Beach.
The app surfline charges 15$ a month for a surf forecast from data that is free to use provided by NOAA. 


# LiveBouy 
Description

This code retrieves current data from the National Oceanic and Atmospheric Administration (NOAA) for spectral wave data from a buoy near a surf spot. It then cleans the data, creates a Pandas DataFrame, and plots the wave height over time. Additionally, the code prints out ideal conditions for surfing, as well as the current conditions for swell direction, swell period, wind, and wave height. Finally, the code retrieves air temperature data from another NOAA buoy.

# Requirements

The following packages are required to run this code:
numpy
pandas
matplotlib

# Usage

Download the script to your local machine.
Ensure that the required packages are installed on your machine.
Run the script with live_bouy.py

# How It Works

The script retrieves spectral wave data from a specific NOAA buoy in real-time using an HTTP request. It then processes and cleans the data, creates a Pandas DataFrame, and plots the wave height over time. The script also prints out the ideal conditions for surfing and the current conditions for swell direction, swell period, wind, and wave height. Finally, the script retrieves air temperature data from another NOAA buoy.

# Known Issues

None known at this time.


# Cloning
git clone https://github.com/MicahHarlan/SurfForecast.git

# Examples of Running it.
![wave_height](https://user-images.githubusercontent.com/81989762/233119310-437a7011-fe9b-4d78-a46b-45fc2bce3427.png)
This shows the variance of wave heights in meters for the date Wednesday April 19th 2023. This can be useful to see how big/small 
ocean waves were through out the day. 

