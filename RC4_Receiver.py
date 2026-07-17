from Crypto.Cipher import ARC4

def receiver():
    try:
        with open("encrypted_message.bin", "rb") as f:
            ciphertext = f.read()

        key = input("Enter Secret Key: ").encode()

        cipher = ARC4.new(key)

        plaintext = cipher.decrypt(ciphertext)

        try:
            print("Decrypted Message:", plaintext.decode())
        except UnicodeDecodeError:
            print("Wrong Key!")

    except FileNotFoundError:
        print("encrypted_message.bin not found. Run Sender first.")

if __name__ == "__main__":
    receiver()
