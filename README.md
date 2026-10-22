# Image Encryption Tool

Simple AES-128-CBC image encryption/decryption using Python and PyCryptodome.

## Features

- Encrypt any image file to `.bin`
- Decrypt `.bin` back to original image
- Configurable encryption key (SHA-256 derived)
- Cross-platform (Linux, macOS, Windows)

## Installation

```bash
git clone https://github.com/yourusername/image-encryption.git
cd image-encryption
pip install -r requirements.txt
```

## Usage

### Encrypt an image

```bash
python encrypt.py path/to/image.jpg
# Uses default key "mysecretpassword", saves to ~/Desktop/encrypted_image.bin

# Custom key and output path
python encrypt.py path/to/image.jpg -k "your-secret-key" -o /path/to/output.bin
```

### Decrypt an image

```bash
python decrypt.py path/to/encrypted_image.bin
# Uses default key, saves as decrypted_image.jpg in same directory

# Custom key and output path
python decrypt.py path/to/encrypted_image.bin -k "your-secret-key" -o /path/to/output.jpg
```

## How it works

- **Algorithm**: AES-128-CBC
- **Key derivation**: SHA-256(password) → first 16 bytes
- **IV**: Randomly generated per encryption, prepended to ciphertext
- **Padding**: PKCS#7 (via `Crypto.Util.Padding`)

## Security notes

- This is a learning/toy implementation
- For production use, consider: authenticated encryption (AES-GC), proper key management, secure random IVs
- Never hardcode keys in real applications

## License

MIT