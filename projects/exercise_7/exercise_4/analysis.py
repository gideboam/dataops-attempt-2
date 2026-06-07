import pandas as pd
import matplotlib.pyplot as plt
# Load the generated dataset
df = pd.read_csv("../src/sensor_data.csv")

# Show first few rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nData Info:")
print(df.info())
print("\nTemperature Statistics:")

print("Average Temperature:", df["temperature"].mean())
print("Max Temperature:", df["temperature"].max())
print("Min Temperature:", df["temperature"].min())
print("\nTop 5 Hottest Readings:")

top5 = df.sort_values(by="temperature", ascending=False).head(5)
print(top5)

# Convert timestamp FIRST (important)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# -------------------------
# Histogram
# -------------------------
plt.figure()
plt.hist(df["temperature"], bins=20)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("histogram.png")

# -------------------------
# Time Series
# -------------------------
plt.figure()
plt.plot(df["timestamp"], df["temperature"])
plt.title("Temperature Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("timeseries.png")
report = df.groupby("device_id")["temperature"].agg([
    "mean", "max", "min"
])

report.to_csv("report.csv")

print("\nReport saved as report.csv")
