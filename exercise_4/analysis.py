import pandas as pd
import matplotlib.pyplot as plt

# Load data from Exercise 3
df = pd.read_csv("../exercise_3/sensor_data.csv")

# Average temperature
avg_temp = df["temperature"].mean()

# Maximum temperature
max_temp = df["temperature"].max()

# Minimum temperature
min_temp = df["temperature"].min()

# Top 5 hottest readings
top_5 = df.sort_values(
    by="temperature",
    ascending=False
).head(5)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort by timestamp
df = df.sort_values("timestamp")

# Histogram
plt.figure()
plt.hist(df["temperature"], bins=20)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()

# Time-series plot
plt.figure()
plt.plot(df["timestamp"], df["temperature"])
plt.title("Temperature Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("timeseries.png")
plt.close()

# Export report
report = pd.DataFrame({
    "Metric": [
        "Average Temperature",
        "Maximum Temperature",
        "Minimum Temperature"
    ],
    "Value": [
        avg_temp,
        max_temp,
        min_temp
    ]
})

report.to_csv("report.csv", index=False)

print("Analysis Complete!")
print(f"Average Temperature: {avg_temp}")
print(f"Maximum Temperature: {max_temp}")
print(f"Minimum Temperature: {min_temp}")
print("\nTop 5 hottest readings:")
print(top_5)
