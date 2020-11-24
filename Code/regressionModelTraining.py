# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:10:31 2017

@author: Aman Kumar
"""

# Fuction to predict land evaluations based on values of parameters given by user
#Importing libraries
import numpy as np
import pandas as pd

def regression(option_selected,bedroom,bathroom,area):
    #Data preprocessing

    #Importing the dataset
    dataset = pd.read_csv('RealEstateCSV.csv')


    #creating a matrix of independent variables/features
    x = dataset.iloc[ : , :-1].values 
    #for dependent variable
    y = dataset.iloc[ : , 4].values



    
    #encoding categorical data
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_x = LabelEncoder()
    x[:,0]=labelencoder_x.fit_transform(x[:,0])
    onehotencoder = OneHotEncoder(categorical_features = [0])
    x = onehotencoder.fit_transform(x).toarray()

    #creating a copy of x will be used in feature scaling of the single sample later
    from copy import deepcopy
    other_x = deepcopy(x)


    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_x = StandardScaler()

    x = sc_x.fit_transform(x)



    #training the RandomForest model 
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 325, random_state = 0)
    regressor.fit(x,y)

        
    input_data = []
    #constructing input array for inputing into prediction model for prediction
    for i in range(0,15):
        if i == option_selected:
            input_data.append(float(1))
        else:
            input_data.append(float(0))
        
    input_data.append(bedroom)
    input_data.append(bathroom)
    input_data.append(area)

    input_data=np.asarray(input_data)

    other_x = np.vstack([other_x,input_data])

    #feature scaling
    from sklearn.preprocessing import StandardScaler
    sc_otherx = StandardScaler()

    other_x = sc_otherx.fit_transform(other_x)

    input_data = other_x[-1]
    data = input_data


    input_data = np.vstack([input_data,data])
    

    prediction = regressor.predict(input_data[:])
    return (prediction[0])
    
