# Image Encryption Tool

Simple image encryption/decryption with **two interfaces**:
- **CLI** (Python, AES-128-CBC)
- **Web** (browser, AES-GCM, no install, works offline)

## Features

- Encrypt any image → `.bin` file
- Decrypt `.bin` → original image
- Configurable password/key
- Cross-platform (Linux, macOS, Windows)
- **Web version runs entirely in your browser — no uploads, no server**

---

## CLI Usage (Python)

### Install
```bash
git clone https://github.com/Abela8767/Image-Encryption.git
cd Image-Encryption
pip install -r requirements.txt
```

### Encrypt
```bash
python encrypt.py path/to/image.jpg
# Default key "mysecretpassword", saves to ~/Desktop/encrypted_image.bin

# Custom key & output
python encrypt.py path/to/image.jpg -k "your-secret-key" -o /path/to/output.bin
```

### Decrypt
```bash
python decrypt.py path/to/encrypted_image.bin
# Default key, saves as decrypted_image.jpg in same directory

# Custom key & output
python decrypt.py path/to/encrypted_image.bin -k "your-secret-key" -o /path/to/output.jpg
```

---

## Web Interface (No Install, Free Hosting)

### Try it locally
Open `web/index.html` directly in your browser — works offline.

### Deploy free on GitHub Pages
1. Go to your repo → **Settings** → **Pages** (left sidebar)
2. **Source**: "Deploy from a branch"
3. **Branch**: `main` → `/web` folder → **Save**
4. Wait ~1 minute → live at `https://Abela8767.github.io/Image-Encryption/`

### Web features
- Drag & drop image → encrypt → downloads `.bin`
- Drag & drop `.bin` → decrypt → downloads image
- Password-based key derivation (PBKDF2, 100k iterations)
- AES-GCM (authenticated encryption)
- Works offline after first load
- Zero server — everything client-side

---

## How it works

| | CLI | Web |
|--|-----|-----|
| **Algorithm** | AES-128-CBC | AES-256-GCM |
| **Key derivation** | SHA-256 → 16 bytes | PBKDF2-SHA256 (100k iter) |
| **IV/Nonce** | Random 16-byte, prepended | Random 12-byte, prepended |
| **Auth tag** | No (CBC) | Yes (GCM) |
| **Format** | `IV + ciphertext` | `salt + IV + ciphertext` |

---

## Security notes

- **Learning/toy implementation** — not audited
- CLI uses CBC (no authentication); Web uses GCM (authenticated)
- For production: use age, GPG, or libsodium
- Never hardcode keys in real applications
- Web version: password never leaves your browser

---

## License

MIT