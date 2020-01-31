#!/usr/bin/python3

import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',header = None, usecols = [0,1,2])

df.columns = ["Class","Alcohol","Malic"]

print(df.head())

from sklearn.preprocessing import StandardScaler

scaling = StandardScaler()

print(scaling.fit_transform(df[['Alcohol','Malic']]))
