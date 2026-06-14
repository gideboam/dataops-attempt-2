import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (from Exercise 3)
df = pd.read_csv("../sensor_data.csv")

# -----------------------------
# 1. Average temperature
# -----------------------------
avg_temp = df["temperature"].mean()

# -----------------------------
# 2. Max and Min temperature
# -----------------------------
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()

# -----------------------------
# 3. Top 5 hottest readings
# -----------------------------
top_5 = df.sort_values(by="temperature", ascending=False).head(5)

# -----------------------------
# 4. Convert timestamp to datetime
# -----------------------------
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort by time (important for time series)
df = df.sort_values(by="timestamp")

# -----------------------------
# 5. Histogram of temperature
# -----------------------------
plt.figure()
plt.hist(df["temperature"], bins=20)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()

# -----------------------------
# 6. Time-series plot
# -----------------------------
plt.figure()
plt.plot(df["timestamp"], df["temperature"])
plt.title("Temperature Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("timeseries.png")
plt.close()

# -----------------------------
# 7. Create report.csv
# -----------------------------
report = pd.DataFrame({
    "Metric": ["Average Temperature", "Max Temperature", "Min Temperature"],
    "Value": [avg_temp, max_temp, min_temp]
})

report.to_csv("report.csv", index=False)

# -----------------------------
# 8. Print summary (for mentor)
# -----------------------------
print("Analysis Complete!")
print(f"Average Temperature: {avg_temp}")
print(f"Max Temperature: {max_temp}")
print(f"Min Temperature: {min_temp}")
print("Top 5 hottest readings:")
print(top_5)
