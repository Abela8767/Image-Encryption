import os
import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib


def decrypt_image(ciphertext, key):
    """Decrypts an image encrypted with AES."""
    try:
        iv = ciphertext[:16]
        ct = ciphertext[16:]

        hashed_key = hashlib.sha256(key.encode()).digest()
        key = hashed_key[:16]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)

        return pt
    except (ValueError, KeyError) as e:
        print(f"Decryption error: {e}. Incorrect Key?")
        return None
    except Exception as e:
        print(f"Decryption Error: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decrypt an AES-encrypted image")
    parser.add_argument("encrypted_file", help="Path to the encrypted .bin file")
    parser.add_argument("-k", "--key", default="mysecretpassword", help="Decryption key (default: mysecretpassword)")
    parser.add_argument("-o", "--output", help="Output path for decrypted image (default: same dir as input, named decrypted_image.jpg)")

    args = parser.parse_args()

    if not os.path.exists(args.encrypted_file):
        print(f"Error: Encrypted file not found at {args.encrypted_file}")
        exit(1)

    with open(args.encrypted_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_image(encrypted_data, args.key)

    if decrypted_data:
        if args.output:
            decrypted_image_path = args.output
        else:
            decrypted_image_path = os.path.join(os.path.dirname(args.encrypted_file), "decrypted_image.jpg")

        with open(decrypted_image_path, "wb") as f:
            f.write(decrypted_data)
        print("Decryption successful! Decrypted image saved as:", decrypted_image_path)
    else:
        print("Decryption failed.")
        exit(1)