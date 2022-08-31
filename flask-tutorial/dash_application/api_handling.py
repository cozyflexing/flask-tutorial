from urllib import response
import pandas as pd
import requests

api_list = {
    "NASDAQ": "https://data.nasdaq.com/api/v3/datasets/CFTC/209742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "SP500": "https://data.nasdaq.com/api/v3/datasets/CFTC/13874A_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "DJIA": "https://data.nasdaq.com/api/v3/datasets/CFTC/124601_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "GOLD": "https://data.nasdaq.com/api/v3/datasets/CFTC/088691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "SILVER": "https://data.nasdaq.com/api/v3/datasets/CFTC/084691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "EURO": "https://data.nasdaq.com/api/v3/datasets/CFTC/099741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "USD": "https://data.nasdaq.com/api/v3/datasets/CFTC/098662_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "GBP": "https://data.nasdaq.com/api/v3/datasets/CFTC/096742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "CAD": "https://data.nasdaq.com/api/v3/datasets/CFTC/090741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "JPY": "https://data.nasdaq.com/api/v3/datasets/CFTC/097741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "AUD": "https://data.nasdaq.com/api/v3/datasets/CFTC/232741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "NZD": "https://data.nasdaq.com/api/v3/datasets/CFTC/112741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "CHF": "https://data.nasdaq.com/api/v3/datasets/CFTC/092741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "WTI": "https://data.nasdaq.com/api/v3/datasets/CFTC/067651_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
    "DJIA": "https://data.nasdaq.com/api/v3/datasets/CFTC/124603_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3",
}

for x in api_list:
    response = requests.get(f"{api_list[x]}")
    with open(f"data/CFTC_{x}.csv", "w+") as f:
        f.write(response.text)
    data = pd.read_csv(f"data/CFTC_{x}.csv")
    data["Commercial Net Position"] = data["Commercial Long"] - data["Commercial Short"]
    data["Noncommercial Net Position"] = (
        data["Noncommercial Long"] - data["Noncommercial Short"]
    )
    data_csv = data.to_csv(
        path_or_buf=f"data/CFTC_{x}.csv",
        sep=",",
        columns=[
            "Date",
            "Open Interest",
            "Noncommercial Long",
            "Noncommercial Short",
            "Noncommercial Spreads",
            "Commercial Long",
            "Commercial Short",
            "Total Long",
            "Total Short",
            "Nonreportable Positions Long",
            "Nonreportable Positions Short",
            "Commercial Net Position",
            "Noncommercial Net Position",
        ],
        header=True,
        index=True,
        encoding=None,
        compression="infer",
        date_format=None,
    )
