# -*- coding: utf-8 -*-
"""datathon lr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P0dWroxAED_ob74tTTl3yzgspUieIhN3

# Linear Regression
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data into a Pandas DataFrame
df1 = pd.read_csv("data1.csv")

# Define the dependent and independent variables for regression model 5
X = df1["Grayscale_Contrast"].values.reshape(-1, 1)
y = df1["Time_Taken"].values

print(X)
print(y)
# Fit the linear regression model
model1 = LinearRegression()
model1.fit(X, y)
 
df2 = pd.read_csv("data2.csv") 
# Define the dependent and independent variables for regression model 6
X = df2["Grayscale_Value"].values.reshape(-1, 1)
print(type(X))


y = df2["Accuracy"].values

# Fit the linear regression model
model2 = LinearRegression()
model2.fit(X, y)

# Define new data for which you want to make predictions
new_data = np.array([[100], [200]])

# Use the model5 object to make predictions for the time taken
predictions_time_taken = model1.predict(new_data)
print(predictions_time_taken)

# Use the model6 object to make predictions for the accuracy
predictions_accuracy = model2.predict(new_data)
print(predictions_accuracy)

import matplotlib.pyplot as plt

# Plot the original data points
plt.scatter(df1["Grayscale_Contrast"], df1["Time_Taken"], color = "red")

# Plot the regression line
plt.plot(df1["Grayscale_Contrast"], model5.predict(df1[["Grayscale_Contrast"]]), color = "blue")

# Add labels and title to the plot
plt.xlabel("Grayscale Contrast")
plt.ylabel("Time Taken")
plt.title("Linear Regression Model 1")

# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Plot the original data points
plt.scatter(df2["Grayscale_Value"], df2["Accuracy"], color = "red")

# Plot the regression line
plt.plot(df2["Grayscale_Value"], model2.predict(df2[["Accuracy"]]), color = "blue")

# Add labels and title to the plot
plt.xlabel("Grayscale Value")
plt.ylabel("Accuracy")
plt.title("Grayscale Value vs Accuracy")

# Show the plot
plt.show()

