import os
import base58
from dotenv import load_dotenv

load_dotenv()


base58_encoded_key = os.getenv('BASE58_ENCODED_KEY')

if base58_encoded_key:
    
    decoded_bytes = base58.b58decode(base58_encoded_key)

    
    key_array = list(decoded_bytes)

    print("Base58 Encoded:", base58_encoded_key)
    print("Array of integers:", key_array)
else:
    print("No Base58 encoded key found in .env file.")
