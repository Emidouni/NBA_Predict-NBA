# NBA Career Prediction Project

# Overview

This project aims to predict the career longevity of NBA players based on their performance statistics. The objective is to predict whether a player will have a career that lasts more than 5 years (Class 1) or less than 5 years (Class 0). The project includes two Jupyter notebooks:

- **EDA (Exploratory Data Analysis) Notebook**: Contains all the steps of data analysis, cleaning, and feature engineering to prepare the dataset for modeling.
- **Modeling Notebook**: Contains a list of models tested, including the best-performing model, which generalizes the best for the prediction task.

## Best Model

After testing different models, **SVM** was selected as the best model for predicting whether a player will have a career lasting more than 5 years or less than 5 years. The best parameters for the SVM model are:
- `C`: 0.1
- `gamma`: 'scale'
- `kernel`: 'linear'

## Streamlit Application

A **Streamlit app** has been developed to allow users to input data and predict whether an NBA player will have a long or short career. You can access the app at:
- [NBA Career Prediction App](https://nbapredict-nba-j3wppsdrxe2hy4orobkp93.streamlit.app/)
