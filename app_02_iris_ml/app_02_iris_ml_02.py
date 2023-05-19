# importing the packages
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
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


def welcome():
    return "Weclome All"


# defining the function which will make the prediction using the data which the user inputs
def prediction(sepal_length, sepal_width, petal_length, petal_width):
    prediction = classifier.predict(
        [[sepal_length, sepal_width, petal_length, petal_width]]
    )
    print(prediction)
    return prediction


# this is the function in which we define out webpage
def main():
    # giving the webpage a title
    st.title("Iris Flower Prediction")

    # the following lines create text boxes in which the user can enter the data required to make the prediction
    sepal_length = st.text_input("Sepal Length")
    sepal_width = st.text_input("Sepal Width")
    petal_length = st.text_input("Petal Length")
    petal_width = st.text_input("Petal Width")
    ans = ""
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked, the prediction funciton defined above is caleld to make the prediction and store it in the variable result
    if st.button("Predict"):
        ans = prediction(sepal_length, sepal_width, petal_length, petal_width)
        if ans == [0]:
            result = "Iris-setosa"
        elif ans == [1]:
            result = "Iris-versicolor"
        elif ans == [2]:
            result = "Iris-virginica"
        st.success("The Species is {}".format(result))


if __name__ == "__main__":
    main()
