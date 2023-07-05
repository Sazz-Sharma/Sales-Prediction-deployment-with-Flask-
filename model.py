import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle
df = pd.read_csv('market_sales.csv')

df['TV'].fillna(df['TV'].mean(), inplace = True)
df['Radio'].fillna(df['Radio'].mean(), inplace = True)
df['Social Media'].fillna(df['Social Media'].median(), inplace = True)
df['Sales'].fillna(df['Sales'].mean(), inplace = True)


df['Influencer'].replace(['Mega','Macro', 'Micro', 'Nano'], [4,3,2,1], inplace = True)
df['zScore']=(df['Sales']-df['Sales'].mean())/df['Sales'].std()
df = df[(df.zScore >=-3) & (df.zScore<=3)]


Xtrain,Xtest,yTrain,yTest = train_test_split(df.iloc[:,:4], df['Sales'], test_size = 0.15)
regressor = LinearRegression()
regressor.fit(Xtrain,yTrain)


pickle.dump(regressor, open('model.pkl', 'wb'))
