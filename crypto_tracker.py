import requests
import pandas as pd
from datetime import datetime

# Get Bitcoin & Ethereum price
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
data = requests.get(url).json()

# Convert to DataFrame
df = pd.DataFrame([{
    "timestamp": datetime.now(),
    "bitcoin_usd": data["bitcoin"]["usd"],
    "ethereum_usd": data["ethereum"]["usd"]
}])

# Save locally
df.to_csv("crypto_prices.csv", index=False)
print("CSV saved:", df)