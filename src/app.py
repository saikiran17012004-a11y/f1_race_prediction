from flask import Flask, render_template, request  
import pandas as pd  
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import StandardScaler 
# Setup Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# 1. Load Data & Train Model (Happens once when the server starts)
df = pd.read_csv('../data/f1_dataset.csv')

# Define features used in training
features = ['GridPosition', 'Points', 'TotalPitTime', 'AvgAirTemp']
X = df[features]
y = df['Position']

# Initialize and fit scaler and model
scaler = StandardScaler()
model = LinearRegression()

# Scale and train
X_scaled = scaler.fit_transform(X)
model.fit(X_scaled, y)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get inputs from the HTML form
        try:
            grid = float(request.form['grid'])
            points = float(request.form['points'])
            pit_time = float(request.form['pit_time'])
            temp = float(request.form['temp'])
            
            # Create a DataFrame for the new input
            user_input = pd.DataFrame([[grid, points, pit_time, temp]], columns=features)
            
            # CRITICAL: Use the SAME scaler to transform input
            user_input_scaled = scaler.transform(user_input)
            
            # Predict
            pred = model.predict(user_input_scaled)
            prediction = f"Predicted Finish Position: {round(pred[0], 1)}"
            
        except Exception as e:
            prediction = f"Error: {str(e)}"
            
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)