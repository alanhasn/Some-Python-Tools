import base64 

"""

This script provides a simple command-line tool
for encrypting and decrypting text using a basic key-based method.
It uses base64 encoding for the encryption and decryption process.
The script prompts the user to enter a mode (encrypt or decrypt),
the text to be processed, and a secret key. Depending on the mode selected, 
it either encrypts or decrypts the text using the provided key.

"""

# Encrypt function
def encrypt(text, key):
    if key == "1234":
        # Convert the text and key to bytes
        text_bytes = text.encode('utf-8')
        key_bytes = key.encode('utf-8')

        # Perform encryption
        encrypted_bytes = base64.b64encode(text_bytes + key_bytes)
        encrypted_text = encrypted_bytes.decode('utf-8')
        return encrypted_text
    else:
        return "Invalid encryption key!"

# Decrypt function
def decrypt(encrypted_text, key):
    try:
        if key == "4321":
            # Convert the encrypted text and key to bytes
            encrypted_bytes = encrypted_text.encode('utf-8')
            key_bytes = key.encode('utf-8')

            # Perform decryption
            decrypted_bytes = base64.b64decode(encrypted_bytes)
            decrypted_text = decrypted_bytes[:-len(key_bytes)].decode('utf-8') # Remove the key bytes from the decrypted text
            return decrypted_text
        else:
            return "Invalid decryption key!"
    except Exception as e:
        return f"Decryption failed: {str(e)}"

# Main function
def main():
    print("Welcome to the Encrypt and Decrypt Tool!")
    mode = input("Enter mode (encrypt or decrypt): ").strip().lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the text: ").strip()
    key = input("Enter the secret key: ").strip()

    if mode == "encrypt":
        result = encrypt(text, key)
    elif mode == "decrypt":
        result = decrypt(text, key)

    print("Result:", result)

if __name__ == "__main__":
    main()