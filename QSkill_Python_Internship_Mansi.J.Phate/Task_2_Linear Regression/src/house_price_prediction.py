import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# Load dataset safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "house_prices.csv")

data = pd.read_csv(csv_path)

# Features and target
X = data[['Size']]
y = data['Price']

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted_price = model.predict(pd.DataFrame([[1600]], columns=["Size"]))
print("Predicted price for 1600 sq ft house:", predicted_price[0])

# Plot regression
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price")
plt.title("House Price Prediction using Linear Regression")
plt.savefig(os.path.join(BASE_DIR, "..", "output", "regression_plot.png"))
plt.show()
