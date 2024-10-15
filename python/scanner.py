from termcolor import colored, cprint
from config import *
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import requests

# replace with your module or variable api key
import dontshare as ds

def main():
    url = "https://public-api.birdeye.so/public/tokenlist"
    headers = {"x-chain": "solana", "X-api-key": ds.birdeye}

    tokens = []
    offset = 0
    limit = -1
    total_tokens = 0
    mc_high = MARKET_CAP_MAX
    mc_low = min_market_cap_to_scan_for

    # Set minimum liquidity and minimum 24-hour volume
    min_liquidity = 30000
    min_volume_24h = MIN_24HR_VOLUME

    # Fetch tokens from Birdeye API
    while True:
        response = requests.get(url, headers=headers, params={"offset": offset, "limit": limit})
        data = response.json()
        tokens.extend(data["tokens"])
        total_tokens += len(data["tokens"])
        if len(data["tokens"]) < limit:
            break
        offset += limit

    # Filter tokens based on market cap and liquidity
    filtered_tokens = [token for token in tokens if mc_low <= token["market_cap"] <= mc_high and token["liquidity"] >= min_liquidity and token["volume_24h"] >= min_volume_24h]

    # Fetch wallets for each token and calculate ROI
    wallets_with_roi = []
    for token in filtered_tokens:
        token_address = token["address"]
        wallet_url = f"https://public-api.birdeye.so/public/token/{token_address}/holders"
        response = requests.get(wallet_url, headers=headers)
        data = response.json()
        holders = data["holders"]
        for holder in holders:
            wallet_address = holder["address"]
            balance = holder["balance"]
            roi = calculate_roi(token, balance)  # implement your ROI calculation logic here
            wallets_with_roi.append((wallet_address, roi))

    # Write wallets with ROI to a file
    with open("wallets_with_roi.txt", "w") as f:
        for wallet_address, roi in wallets_with_roi:
            f.write(f"{wallet_address}: {roi:.2f}%\n")

def calculate_roi(token, balance):
    # implement your ROI calculation logic here
    # for example:
    token_price = token["price"]
    roi = (balance * token_price) / (token["market_cap"] / token["circulating_supply"])
    return roi

if __name__ == "__main__":
    main()