import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Load the data (training)
df = pd.read_csv('../data/f1_dataset.csv')
X = df[['GridPosition', 'Points']]
y = df['Position']

# 2. Train the model one more time
model = LinearRegression()
model.fit(X, y)

# 3.Create a "Hypothetical" scenario for the japanese GP
# Let's see what the model predicts for a driver starting 5th with 10 points
driver_input = pd.DataFrame({'GridPosition': [5], 'Points': [10]})
prediction = model.predict(driver_input)

print("---- 2025 japanese GP Prediction ---")
print(f"If a driver starts 5thand has 10 points...")
print(f"The model predicts a finishing position of: {prediction[0]:.1f}")
