import pandas as pd

# 1. Load the data we just created
df = pd.read_csv('../data/f1_dataset.csv')

# 2. Check the correlation
# We want to see if gridposition is linked to the final position
correlation = df['GridPosition'].corr(df['Position'])

print("----Analysis Report ---")
print(f"Correlation between Grid Position and Final Position: {correlation:2f}")

# 3. Simple interpretation
if correlation > 0.5:
    print("Insight: Strong link! Drivers tend to finish near where they start.")
else:
    print("Insight: The link is weak. Strategy or racepace might be more important.")
    