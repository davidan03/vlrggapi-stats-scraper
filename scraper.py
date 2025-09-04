# importing required libraries
import requests
import pandas as pd
import time

base_url = "https://vlrggapi.vercel.app/stats"
regions = ["na", "eu", "ap", "sa", "jp", "oce", "mn"]

for region in regions:
        response = requests.get(base_url, params={"region": region, "timespan": "all"})
        all_data = response.json()

        # edit to add all regions to the dataframe
        if all_data["data"]["status"] == 200:
            data = all_data["data"]["segments"]
            df = pd.DataFrame(data)
            df.to_csv(f"{region}stats.csv")
        





