import os
import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib


def encrypt_image(image_path, key):
    """Encrypts an image using AES."""
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()

        hashed_key = hashlib.sha256(key.encode()).digest()
        key = hashed_key[:16]

        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(image_data, AES.block_size))
        iv = cipher.iv
        ciphertext = iv + ct_bytes
        return ciphertext
    except Exception as e:
        print(f"Encryption error: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encrypt an image using AES-128-CBC")
    parser.add_argument("image_path", help="Path to the image file to encrypt")
    parser.add_argument("-k", "--key", default="mysecretpassword", help="Encryption key (default: mysecretpassword)")
    parser.add_argument("-o", "--output", help="Output path for encrypted file (default: ~/Desktop/encrypted_image.bin)")

    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: Image not found at {args.image_path}")
        exit(1)

    if args.output:
        encrypted_path = args.output
    else:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        encrypted_path = os.path.join(desktop_path, "encrypted_image.bin")

    print(f"Image path: {args.image_path}")
    print(f"Encrypted path: {encrypted_path}")

    encrypted_data = encrypt_image(args.image_path, args.key)

    if encrypted_data:
        try:
            with open(encrypted_path, "wb") as f:
                f.write(encrypted_data)
            print(f"Image encrypted and saved to: {encrypted_path}")
        except Exception as e:
            print(f"Error saving encrypted file: {e}")
            exit(1)