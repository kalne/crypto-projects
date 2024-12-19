import requests

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json().get(crypto, {}).get("usd")
        if price:
            print(f"The current price of {crypto.capitalize()} is ${price}")
        else:
            print("Error: Could not find price data.")
    else:
        print("Error: API request failed.")

if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    get_crypto_price(crypto)