import hashlib

def calculate_sha256(input_string):
    """Calculates the SHA-256 hash of a given string."""
    encoded_string = input_string.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_string).hexdigest()
    return sha256_hash

if __name__ == "__main__":
    text_to_hash = input("Enter the text you want to hash: ")
    hash_value = calculate_sha256(text_to_hash)
    print(f"The SHA-256 hash of '{text_to_hash}' is: {hash_value}")
