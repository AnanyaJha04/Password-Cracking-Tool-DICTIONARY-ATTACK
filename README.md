# Password Cracking Tool 
# DICTIONARY ATTACK
## Purpose-
The primary purpose of this code is to illustrate how this type of attack works by taking a target SHA-256 hash, comparing it against the hashes of words read from a provided wordlist, and revealing the original password if a match is found. This basic implementation aims to enhance security awareness by showcasing the vulnerability of weak, dictionary-based passwords, which can be used ethically for security testing and auditing with proper authorization.

## Features-
1. Dictionary Attack Implementation: The core feature is its ability to perform a dictionary attack by iterating through a wordlist.
2. SHA-256 Hashing: It utilizes the hashlib library to calculate the SHA-256 hash of each word in the wordlist for comparison.
3. Takes Hashed Password as Input: It prompts the user to enter the SHA-256 hash of the password they want to attempt to crack.
4. Takes Wordlist Path as Input: It requires the user to specify the path to a dictionary file containing potential passwords.
5. Wordlist Processing: It reads the wordlist file line by line, stripping whitespace and newline characters from each word.
6. Hash Comparison: It compares the generated hash of each word with the target hashed password.
7. Password Output: If a match is found, it prints the cracked password to the console.
8. "Not Found" Message: If the entire wordlist is processed without a match, it informs the user that the password was not found in the list.
9. Basic Error Handling: It includes a try-except block to catch FileNotFoundError if the specified wordlist file does not exist, providing a user-friendly error message.
10. Clear Output: It provides clear messages indicating whether the password was cracked or not.

## Terminology-
1. Hashlib- This module provides a way to create one-way functions that take an input (like a string of text, a file, or any data) and produce a fixed-size string of characters called a hash or a digest.
2. Wordlist- It is a text file containing a large collection of potential passwords.
3. SHA-256- It stands for Secure Hash Algorithm 256-bit and is a widely used and highly regarded cryptographic hash function. It's a common hashing algorithm used for storing passwords.
4. Hashed password- It is a one-way encrypted version of a user's password.
5. Encode- It means to convert information or data into a specific format, often a coded form, for storage, transmission, or security purposes.
6. UTF-8- It is a character encoding standard used to represent text, primarily on the web and in other digital contexts.
7. Hexdigest()- It is a method in the code that returns the hash in a hexadecimal format safe for any non-binary presentation.
8. Dictionary Attack- It is an attempt to gain illicit access to a computer system by using a very large set of words to generate potential passwords.
9. Strip()- It is a method in Python that is used to remove leading and trailing characters from a string. By default, it removes whitespace characters such as spaces, tabs, and newlines.

## Limitations-
1. Wordlist Dependent: Only works if the password is in the provided wordlist.
2. Basic Attack: Only performs a simple dictionary attack, no advanced techniques.
3. No Salt Support: Doesn't handle salted password hashes common in real systems.
4. SHA-256 Only: Specifically designed for SHA-256 hashes.
5. Slow for Large Lists: Basic implementation with no speed optimizations.
6. Single-Threaded: Doesn't utilize multiple processing cores.
7. Limited Error Handling: Basic error checking.
8. No Pattern Generation: Can't guess based on character sets or patterns.
9. No Progress Feedback: Doesn't show how far it's progressed.
10. Unrealistic for Modern Security: Ineffective against well-secured passwords.

## Ethical Considerations-
"The ethical use of the password cracking code is strictly limited to situations where explicit legal authorization has been granted, emphasizing respect for privacy and the avoidance of any actions that could lead to harm or unauthorized access. Transparency and responsible disclosure are crucial when used for legitimate security testing, ensuring that findings are shared appropriately. The code should serve as an educational tool for understanding password security vulnerabilities, but always within legal and ethical boundaries, with a firm commitment against malicious intent and a focus on responsible disclosure of any discovered weaknesses."

## Further Improvement-
1. Implement Brute-Force: Add the ability to try all character combinations.
2. Add Rule-Based Cracking: Apply common password modification rules to wordlist entries.
3. Support Rainbow Tables: Integrate pre-computed hash tables for faster lookups.
4. Handle Salts: Modify to process salted password hashes.
5. Support More Hash Algorithms: Extend to crack hashes beyond SHA-256.
6. Multi-Threading/Async: Utilize multiple cores for faster processing.
7. Progress Bar: Show the user the progress of the attack.
8. Character Set/Mask Options: Allow specifying character sets and password structures.
9. Optimize Wordlist Handling: Improve efficiency for large wordlists.
10. Session Management: Allow pausing and resuming cracking attempts.
11. GUI Interface: Create a user-friendly graphical interface.
12. Logging: Record the cracking attempts and results.
13. Rate Limiting (Carefully): Implement delays to mimic realistic login attempts (use with caution and ethically).



