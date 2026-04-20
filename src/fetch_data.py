import fastf1
import os

# 1. Setup the cache directory
cache_dir = '../data'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
fastf1.Cache.enable_cache(cache_dir)

# 2. Let's load the 2025 Bahrain Grand Prix
print("Connecting to the F1 database... (this might take a moment)")
session = fastf1.get_session(2025, 'Bahrain', 'R')
session.load()

# 3. Print the results
print("Data loaded successfully!")
print(session.results[['FullName', 'Position', 'GridPosition']])

# Calculate how many positions each driver gained or lost
# (GridPosition - Position)
session.results['PositionsGained'] = session.results['GridPosition'] - session.results['Position']

# Sort the table to show who gained the most spots
gains = session.results[['FullName', 'PositionsGained']].sort_values(by='PositionsGained', ascending=False)

print("\n--- Who gained the most positions? ---")
print(gains.head())