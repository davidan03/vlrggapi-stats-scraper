import requests
import pandas as pd
import time

base_url = "https://vlrggapi.vercel.app/stats"
regions = ["na", "eu", "ap", "sa", "jp", "oce", "mn"]

# loop through every region
for region in regions:
        response = requests.get(base_url, params={"region": region, "timespan": "all"})
        all_data = response.json() # transform json data into python dict

        # checks that the request was successful
        if all_data["data"]["status"] == 200:
            data = all_data["data"]["segments"]
            df = pd.DataFrame(data)
            df.to_csv(f"{region}stats.csv") # creates csv file for each region
            time.sleep(0.5)
        





