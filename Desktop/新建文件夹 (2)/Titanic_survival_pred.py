"""
The algorithm used in this file is mainly logistic Regression, to predict the number of survivals in the test file.In the end, a CSV file with name "report.csv" will be saved.
The CSV file should contain the following:1, The prediction for survivals with respect to ages and genders
                                          2, etc
"""
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

# import the data
data = pd.read_csv("train.csv")