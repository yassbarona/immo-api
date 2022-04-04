from preprocessing.cleaning_data import preprocess
import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def predictor(df):
    X_test= df.to_numpy()
    pickle_in = open("/immo_api/regressor.pickle", "rb")
    regressor = pickle.load(pickle_in)
    return regressor.predict(X_test)
    