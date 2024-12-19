import requests

def convert_crypto_to_fiat(crypto, amount):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json().get(crypto, {}).get("usd")
        if price:
            converted = amount * price
            print(f"{amount} {crypto.capitalize()} is equivalent to ${converted:.2f}")
        else:
            print("Error: Could not find price data.")
    else:
        print("Error: API request failed.")

if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    amount = float(input("Enter the amount: "))
    convert_crypto_to_fiat(crypto, amount)