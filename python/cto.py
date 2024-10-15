import requests
from datetime import datetime, timedelta

# Dexscreener API endpoint for fetching token pairs
DEXSCREENER_API_URL =  "https://api.dexscreener.com/latest/dex/tokens/"

# Minimum liquidity in USD
MIN_LIQUIDITY = 30000

# Minimum token age in hours
MIN_TOKEN_AGE_HOURS = 24

# Minimum number of tokens traded by wallet
MIN_TOKENS_TRADED = 3

# Simulate a method to fetch wallet transaction details (you would use a proper API for this)
def get_wallet_transactions(wallet_address):
    """
    Mock function to fetch wallet transactions.
    In reality, this function should call an API that can provide wallet transaction history.
    Returns a list of token addresses that the wallet has interacted with.
    """
    # Example data: Simulated token addresses the wallet has traded
    # You'd fetch actual transaction data using an API (like Solscan or Dexscreener)
    simulated_token_trades = [
        "TokenA", "TokenB", "TokenC", "TokenD",  # 4 tokens traded
        "TokenE", "TokenF"
    ]
    return simulated_token_trades


def fetch_token_listings():
    """Fetches token listings from the Dexscreener API."""
    try:
        response = requests.get(DEXSCREENER_API_URL)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json().get("pairs", [])
    except requests.RequestException as e:
        print(f"Error fetching token listings: {e}")
        return []

def filter_tokens(tokens):
    """Filters tokens by liquidity and creation date criteria."""
    valid_tokens = []
    # Calculate the time 48 hours ago
    time_threshold = datetime.now() - timedelta(hours=MIN_TOKEN_AGE_HOURS)

    for token in tokens:
        # Fetch liquidity in USD
        liquidity = token.get("liquidity", {}).get("usd", 0)

        # Fetch token creation time
        creation_time_str = token.get("baseToken", {}).get("creationTime", "")

        if not creation_time_str:
            continue

        try:
            # Convert the creation time to a datetime object
            creation_time = datetime.strptime(creation_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            # Skip token if the creation date is not formatted properly
            continue

        # Check if the token meets the liquidity and age criteria
        if liquidity >= MIN_LIQUIDITY and creation_time <= time_threshold:
            valid_tokens.append({
                "name": token.get("baseToken", {}).get("name"),
                "symbol": token.get("baseToken", {}).get("symbol"),
                "liquidity": liquidity,
                "creation_time": creation_time_str,
                "wallets": token.get("holders", [])  # Assuming Dexscreener provides wallet info (or use Solscan)
            })

    return valid_tokens

def check_wallets_activity(wallets):
    """
    Checks the activity of wallets, ensuring they have traded at least 4 tokens.
    Returns a list of wallets that meet the criteria.
    """
    active_wallets = []
    
    for wallet in wallets:
        # Fetch the wallet's transactions (or token trades)
        tokens_traded = get_wallet_transactions(wallet)

        # Check if the wallet has traded at least 4 different tokens
        if len(tokens_traded) >= MIN_TOKENS_TRADED:
            active_wallets.append(wallet)
    
    return active_wallets

def run_cto_scanner():
    """Runs the CTO scanner."""
    print("Fetching token listings from Dexscreener...")
    tokens = fetch_token_listings()

    if not tokens:
        print("No tokens fetched.")
        return

    print(f"Fetched {len(tokens)} tokens. Filtering tokens by liquidity and creation date...")

    # Filter tokens by liquidity and creation date
    filtered_tokens = filter_tokens(tokens)

    if filtered_tokens:
        print(f"Found {len(filtered_tokens)} tokens that match the criteria:")
        for token in filtered_tokens:
            print(f"\nToken: {token['name']} ({token['symbol']}), Liquidity: ${token['liquidity']}, Created at: {token['creation_time']}")

            # Check wallets associated with the token for fresh activity
            wallets = token.get("wallets", [])
            active_wallets = check_wallets_activity(wallets)

            if active_wallets:
                print(f"  Active wallets with at least 4 tokens traded:")
                for wallet in active_wallets:
                    print(f"    - Wallet: {wallet}")
            else:
                print(f"  No active wallets found with enough token trades.")
    else:
        print("No tokens matched the criteria.")

if __name__ == "__main__":
    run_cto_scanner()
