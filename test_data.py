import numpy as np
import pandas as pd

# Define the column names based on the 17 sensor readings
sensor_columns = [
    "pressure_readings_1", "pressure_readings_2", "pressure_readings_3",
    "pressure_readings_4", "pressure_readings_5", "pressure_readings_6",
    "temperature_readings_1", "temperature_readings_2", "temperature_readings_3",
    "temperature_readings_4", "vibration_readings_1", "vibration_readings_2",
    "flow_rate_1", "flow_rate_2", "efficiency_index_1", "efficiency_index_2",
    "cooling_efficiency_ratio"
]

# Define reasonable ranges for synthetic data based on stable cycles
sensor_ranges = {
    "pressure": (50, 200),  # Pressure readings in a stable range
    "temperature": (30, 90),  # Temperature readings in a stable range
    "vibration": (0.1, 1.0),  # Vibration sensor readings
    "flow_rate": (5, 50),  # Flow rate values
    "efficiency_index": (0.7, 1.0),  # Efficiency indices
    "cooling_efficiency_ratio": (0.1, 0.9),  # Cooling efficiency
}

# Generate synthetic data for 60 seconds (60 rows)
num_seconds = 60
synthetic_data = np.column_stack([
    np.random.uniform(*sensor_ranges["pressure"], size=num_seconds) for _ in range(6)
] + [
    np.random.uniform(*sensor_ranges["temperature"], size=num_seconds) for _ in range(4)
] + [
    np.random.uniform(*sensor_ranges["vibration"], size=num_seconds) for _ in range(2)
] + [
    np.random.uniform(*sensor_ranges["flow_rate"], size=num_seconds) for _ in range(2)
] + [
    np.random.uniform(*sensor_ranges["efficiency_index"], size=num_seconds) for _ in range(2)
] + [
    np.random.uniform(*sensor_ranges["cooling_efficiency_ratio"], size=num_seconds)
])

# Create a DataFrame
synthetic_df = pd.DataFrame(synthetic_data, columns=sensor_columns)

# Display the first few rows
print(synthetic_df)
