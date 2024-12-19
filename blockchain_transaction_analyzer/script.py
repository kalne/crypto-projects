import requests

def get_latest_block():
    url = "https://blockchain.info/latestblock"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Latest Block Hash: {data['hash']}")
        print(f"Number of Transactions: {len(data['txIndexes'])}")
    else:
        print("Error: API request failed.")

if __name__ == "__main__":
    get_latest_block()