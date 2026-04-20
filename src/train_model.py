import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Load the data
df = pd.read_csv('../data/f1_dataset.csv')

# 2. Add Team to the features (One-Hot Encoding)
# This turns 'TeamName' into numeric columns like 'Team_Ferrari', 'Team_Red Bull', etc.
df_processed = pd.get_dummies(df, columns=['TeamName'])

# 3. Prepare the data (Now including Team features)
# Use the one-hot encoded dataset and include the new TeamName columns
base_features = ['GridPosition', 'Points', 'TotalPitTime', 'AvgAirTemp']
team_features = [col for col in df_processed.columns if col.startswith('TeamName_')]
features = base_features + team_features
X = df_processed[features]
y = df_processed['Position']

# 4. Split and Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict and check accuracy
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print("--- Improved Model Training ---")
print(f"New Average Error: {error:.2f} positions")