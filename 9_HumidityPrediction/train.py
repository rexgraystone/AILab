import pandas as pd
from sklearn.linear_model import LinearRegression
import json

data = pd.read_csv('data.txt')

# Split the data into input (X) and output (y) variables
X = data[['Temperature']]
y = data['Humidity']

model = LinearRegression()
model.fit(X, y)

# Extract the coefficients and intercept from the trained model
coefficients = model.coef_[0]
intercept = model.intercept_

model_data = {
    'coefficients': coefficients,
    'intercept': intercept
}

with open('model.json', 'w') as f:
    json.dump(model_data, f)