import pandas as pd
import random
from datetime import datetime

data = {
    "id": [random.randint(1000, 9999) for _ in range(5)],
    "value": [random.random() for _ in range(5)],
    "timestamp": [datetime.now().isoformat() for _ in range(5)]
}

df = pd.DataFrame(data)

df.to_csv("data/generated_data.csv", index=False)

print("Data generated successfully")
