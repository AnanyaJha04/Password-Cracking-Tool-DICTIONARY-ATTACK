import hashlib
def crack_password(hashed_password, wordlist_path):
    try:
        with open(wordlist_path, 'r') as wordlist_file:
            for word in wordlist_file:
                word = word.strip()  # Remove leading/trailing whitespace and newline
                encoded_word = word.encode('utf-8')
                hashed_candidate = hashlib.sha256(encoded_word).hexdigest()
                if hashed_candidate == hashed_password:
                    return word
    except FileNotFoundError:
        print(f"Error: Wordlist file not found at {wordlist_path}")
        return None
    return None

if __name__ == "__main__":
    hashed_target = input("Enter the SHA-256 hash of the password to crack: ")
    wordlist_file = input("Enter the path to the wordlist file: ")

    cracked_password = crack_password(hashed_target, wordlist_file)

    if cracked_password:
        print(f"Password cracked! The password is: {cracked_password}")
    else:
        print("Password not found in the wordlist.")
