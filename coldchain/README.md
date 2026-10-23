# Cold Chain Analysis Project

This project analyzes cold chain logistics data to monitor and optimize temperature-sensitive shipments across various commodities including dairy, pharmaceuticals, frozen foods, and fresh produce.

## Project Overview

The cold chain analysis project tracks shipments, telemetry data, weather conditions, and food loss context to identify patterns, optimize logistics, and reduce spoilage in temperature-sensitive supply chains.

## Project Structure

```
coldchain/
├── cold chain analysys.pbix    # Power BI dashboard for visualization
├── data/
│   ├── raw/                     # Raw input datasets
│   │   ├── shipments.csv         # Shipment logistics data
│   │   ├── telemetry.csv        # IoT sensor readings (temperature, humidity)
│   │   ├── weather.csv          # Weather conditions data
│   │   └── food_loss_context.csv # Food loss contextual data
│   └── clean/                   # Processed/cleaned datasets
│       ├── cleaned_shipments.csv
│       ├── cleaned_telemetry.csv
│       ├── cleaned_weather.csv
│       └── cleaned_food_loss.csv
└── scripts/
    └── clean_data.py            # Data cleaning and preprocessing script
```

## Data Sources

### Shipments Data (`shipments.csv`)
Contains logistics information for each shipment:
- **shipment_id**: Unique identifier for each shipment
- **commodity**: Type of goods (Dairy, Pharmaceutical, Frozen Food, Fresh Produce)
- **origin/destination**: Location codes (e.g., LOC_BLR, LOC_MUM, LOC_PUN)
- **departure_time/arrival_time**: Timestamps for shipment journey
- **distance_km**: Total distance traveled
- **stop_count**: Number of stops during transit
- **total_stop_minutes**: Total duration of stops
- **vehicle_age_years**: Age of the transport vehicle
- **target_temp_min_c/target_temp_max_c**: Required temperature range
- **synthetic_spoilage_label**: Label indicating spoilage occurrence (0/1)

### Telemetry Data (`telemetry.csv`)
IoT sensor readings from shipment containers:
- **shipment_id**: Reference to shipment
- **recorded_at**: Timestamp of sensor reading
- **internal_temp_c**: Internal temperature in Celsius
- **humidity_pct**: Humidity percentage
- **location_id**: Current location code
- **latitude/longitude**: GPS coordinates

### Weather Data (`weather.csv`)
Weather conditions during shipment transit:
- **weather_time**: Timestamp of weather reading
- **temperature_c**: Ambient temperature
- **humidity_pct**: Relative humidity
- **wind_speed_kmh**: Wind speed
- **precipitation_mm**: Precipitation levels

### Food Loss Context (`food_loss_context.csv`)
Contextual data about food loss patterns and factors.

## Requirements

- Python 3.7+
- pandas

Install dependencies:
```bash
pip install pandas
```

## Usage

### Data Cleaning

Run the data cleaning script to process raw datasets:

```bash
python scripts/clean_data.py
```

This script will:
1. Load raw datasets from `data/raw/`
2. Convert date columns to datetime format
3. Handle missing telemetry values by filling with mean values
4. Export cleaned files to `data/clean/`

### Power BI Dashboard

Open `cold chain analysys.pbix` in Power BI Desktop to explore visualizations and insights from the cleaned data.

## Data Cleaning Process

The `clean_data.py` script performs the following operations:

1. **Date Formatting**: Converts timestamp columns to proper datetime objects
   - `departure_time`, `arrival_time` in shipments
   - `recorded_at` in telemetry
   - `weather_time` in weather data

2. **Missing Value Imputation**: Fills missing telemetry values with column means
   - `internal_temp_c`: Filled with mean temperature
   - `humidity_pct`: Filled with mean humidity

3. **Export**: Saves cleaned datasets to `data/clean/` directory

## Key Metrics Tracked

- Temperature compliance (min/max target ranges)
- Shipment duration and stop patterns
- Vehicle age impact on spoilage
- Environmental conditions (weather, humidity)
- Spoilage rates by commodity type
- Route efficiency (distance, stops, duration)

## License

This project is for internal analysis purposes.
