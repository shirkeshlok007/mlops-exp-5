import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([10, 20, 30, 40])

model = LinearRegression()
model.fit(X, y)

with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")