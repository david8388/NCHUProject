# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import model
import pandas as pd
from pandas import DataFrame as df
import numpy as np
#from sklearn.linear_model import LogisticRegression as LR
import matplotlib.pyplot as plt
#from sklearn.metrics import confusion_matrix
#from sklearn.metrics import classification_report

# Step1: Load data

data = pd.read_csv("2330.csv")

# Step2: Preprocessing data= Prepare X, Y
# 1. imputer for missing data
# 2. feature sizing
# 3. categorical data transform

# Method 1
# X = data['values'].values.reshape(-1,1)
# Y = data['status'].values.reshape(-1,1)

# Method 2
# X = np.array(data['values']).reshape(-1,1)
# Y = np.array(data['status']).reshape(-1,1)

X = data.iloc[:-4,2:7].values.reshape(-1,5)
Y = data.iloc[:-4,-1].values.reshape(-1,1)

# Step3: Build Model

model = LR()
model.fit(X,Y)
predY = model.predict(data.iloc[-3,2:7].values.reshape(-1,5))
#data.iloc[-3, 1]
# Step4: Evaluate Model


# Step5: Predict (write out)

