import random
import csv

# Define the manufacturer recommended values with their +/- 50% ranges
properties = {
    "Useable Energy": (4, 2),  # kWh
    "Max Cont. Charge/Discharge Current": (65, 32.5),  # A
    "Peak Output Current": (90, 45),  # A
    "Weight": (64, 32),  # kg
    "Rated DC Power": (3.3, 1.65),  # kW
    "Nominal Voltage": (51.2, 25.6),  # V
    "Operating Voltage": (51.2, 25.6),  # V
    "Operating Temperature": (20, 10),  # °C
    "Round-Trip Efficiency": (0.95, 0.475),  # %
    "Warranty": (10, 5)  # years
}

# Generate datasets for 100 batteries
num_batteries = 100
filename = "battery_datasets.csv"
with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=properties.keys())
    writer.writeheader()
    
    for i in range(1, num_batteries + 1):
        battery_data = {}
        for property_name, (mean, half_range) in properties.items():
            # Generate a value within the specified range
            value = round(random.uniform(mean - half_range, mean + half_range), 2)
            battery_data[property_name] = value
        
        # Write battery data to the CSV file
        writer.writerow(battery_data)

print(f"All datasets have been generated and saved to '{filename}'.")
