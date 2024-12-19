import secrets

def generate_wallet():
    private_key = secrets.token_hex(32)
    print(f"Your new private key: {private_key}")

if __name__ == "__main__":
    generate_wallet()