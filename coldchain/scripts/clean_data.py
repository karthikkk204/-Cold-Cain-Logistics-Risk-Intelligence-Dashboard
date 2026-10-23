import pandas as pd
import os

# Get the exact directory where this script is currently located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Since script is in coldchain/scripts/, going up ONE level (..) reaches coldchain/ (project root)
project_root = os.path.abspath(os.path.join(script_dir, '..'))
raw_dir = os.path.join(project_root, 'data', 'raw')
clean_dir = os.path.join(project_root, 'data', 'clean')

os.makedirs(clean_dir, exist_ok=True)

print(f"Looking for raw files in: {raw_dir}")

# 1. Load raw datasets
shipments = pd.read_csv(os.path.join(raw_dir, 'shipments.csv'))
telemetry = pd.read_csv(os.path.join(raw_dir, 'telemetry.csv'))
weather = pd.read_csv(os.path.join(raw_dir, 'weather.csv'))
food_loss = pd.read_csv(os.path.join(raw_dir, 'food_loss_context.csv'))

# 2. Clean and format dates
shipments['departure_time'] = pd.to_datetime(shipments['departure_time'])
shipments['arrival_time'] = pd.to_datetime(shipments['arrival_time'])
telemetry['recorded_at'] = pd.to_datetime(telemetry['recorded_at'])
weather['weather_time'] = pd.to_datetime(weather['weather_time'])

# 3. Handle missing telemetry values
telemetry['internal_temp_c'] = telemetry['internal_temp_c'].fillna(telemetry['internal_temp_c'].mean())
telemetry['humidity_pct'] = telemetry['humidity_pct'].fillna(telemetry['humidity_pct'].mean())

# 4. Export cleaned files to the clean folder
shipments.to_csv(os.path.join(clean_dir, 'cleaned_shipments.csv'), index=False)
telemetry.to_csv(os.path.join(clean_dir, 'cleaned_telemetry.csv'), index=False)
weather.to_csv(os.path.join(clean_dir, 'cleaned_weather.csv'), index=False)
food_loss.to_csv(os.path.join(clean_dir, 'cleaned_food_loss.csv'), index=False)

print("Data cleaning completed successfully! Clean files saved to data/clean/")