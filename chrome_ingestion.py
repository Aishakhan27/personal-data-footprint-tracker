import json
import pandas as pd
with open("personal-data-footprint-tracker/Data/History.json", "r", encoding="utf-8") as file:
    data = json.load(file)
browser_history = data["Browser History"]
df = pd.DataFrame(browser_history)
df = df[
    [
        "title",
        "url",
        "time_usec",
        "page_transition_qualifier"
    ]
]
df["visited_at"] = pd.to_datetime(df["time_usec"], unit="us")
df.drop(columns=["time_usec"], inplace=True)
df = df[
    [
        "visited_at",
        "title",
        "url",
        "page_transition_qualifier"
    ]
]
print(df.head())
df.to_csv("personal-data-footprint-tracker/chrome_history_cleaned.csv", index=False)
print("Cleaned data saved successfully!")
from database import engine

df.to_sql(
    "chrome_history",
    con=engine,
    if_exists="append",
    index=False
)

print("Data inserted into PostgreSQL successfully!")