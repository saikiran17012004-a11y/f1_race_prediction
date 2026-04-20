import fastf1
import pandas as pd
from datetime import datetime
import os

# 1. Setup cache
if not os.path.exists('../data'):
    os.makedirs('../data')
fastf1.Cache.enable_cache('../data')

def collect_latest_data():
    print("Fetching 2026 F1 Schedule...")
    schedule = fastf1.get_event_schedule(2026)
    
    # 2. Dynamic Event Detection
    # Filter for races that have already happened
    now = datetime.now()
    past_races = schedule[schedule['EventDate'] <= now]
    
    if past_races.empty:
        print("No completed races found for 2026 yet.")
        return

    # Select the most recent race
    latest_race = past_races.iloc[-1]
    event_name = latest_race['EventName']
    print(f"Detected latest race: {event_name}")
    
    # 3. Load Session
    session = fastf1.get_session(2026, event_name, 'R')
    session.load()
    
    # 4. Calculate Pit Stops (from Laps data)
    laps = session.laps
    pit_stops = laps[laps['PitInTime'].notna() & laps['PitOutTime'].notna()].copy()
    pit_stops['Duration'] = pit_stops['PitOutTime'] - pit_stops['PitInTime']
    
    # Aggregate: Sum duration per driver
    total_pit_time = pit_stops.groupby('DriverNumber')['Duration'].sum().dt.total_seconds()
    
    # 5. Get Weather Data
    avg_temp = session.weather_data['AirTemp'].mean()
    
    # 6. Merge into Results
    res = session.results.copy()
    res['TotalPitTime'] = res['DriverNumber'].map(lambda x: total_pit_time.get(x, 0))
    res['AvgAirTemp'] = avg_temp
    res['Race'] = event_name
    
    # 7. Final selection
    final_res = res[['FullName', 'Position', 'GridPosition', 'Points', 'TeamName', 'TotalPitTime', 'AvgAirTemp', 'Race']]
    
    # Save to CSV
    final_res.to_csv('../data/f1_dataset.csv', index=False)
    print(f"Success! Data for {event_name} saved to ../data/f1_dataset.csv")

if __name__ == "__main__":
    collect_latest_data()