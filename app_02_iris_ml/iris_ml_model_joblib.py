# importing the packages
import pandas as pd
import numpy as np
import streamlit as st
import os

# determing the location of the csv file
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "Iris.csv")
# reading the iris dataset
df = pd.read_csv(filename)

# dropping the Id column
df.drop("Id", axis=1, inplace=True)

# Renaming the target column into numbers to aid training of the model
df["Species"] = df["Species"].map(
    {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
)

# splitting the data into the columns which need to be trained(x) and the target column(y)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# splitting the data into training and testing data in the ratio 7:3
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101
)

# importing the RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

# creating an instance for the random forest classifier
classifier = RandomForestClassifier()

# fitting the training data into the dataset
classifier.fit(X_train, y_train)

# predicting on the test dataset
y_pred = classifier.predict(X_test)

# finding out the accuracy
from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, y_pred)

# the accuracy of the model is 95.55% which is very good

##########################################################################################
##########################################################################################

# pickling the model
import joblib

joblib.dump(classifier, "classifier.joblib")
