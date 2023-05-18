# importing the packages
import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image
import os

# determing the location if the pickled model
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "classifier.pkl")

# loading the pickled model to predict on the data
pickle_in = open(filename, "rb")
classifier = pickle.load(pickle_in)


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
        st.success("The Output is {}".format(result))


if __name__ == "__main__":
    main()
