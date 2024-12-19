import requests
import time

def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    return response.json().get(crypto, {}).get("usd")

def alert_price(crypto, target_price):
    while True:
        price = get_crypto_price(crypto)
        if price and price >= target_price:
            print(f"ALERT: {crypto.capitalize()} has reached ${price}")
            break
        time.sleep(60)

if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    target_price = float(input("Enter target price in USD: "))
    alert_price(crypto, target_price)