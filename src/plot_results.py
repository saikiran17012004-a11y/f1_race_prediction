import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 1. Prepare data
df = pd.read_csv('../data/f1_dataset.csv')
X = df[['GridPosition', 'Points', 'TotalPitTime', 'AvgAirTemp']]
y = df['Position']

# 2. Train(same setup as before)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled,y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 3. predict
predictions = model.predict(X_test)

# 4. Plot 
plt.scatter(y_test, predictions, color='blue')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Actual Finishing Position')
plt.ylabel('Predicted Finishing Position')
plt.title('Model Accuracy: Predicted vs. Actual')
plt.show()