# Steganography Mini Task

This mini project involves the use of the **Steghide** tool in Kali Linux to explore the fascinating world of steganography. Steghide allows embedding and extracting data within image or audio files while maintaining the integrity of the carrier file.

## Features
- Embed secret messages or files into carrier files (e.g., images, audio).
- Extract hidden data from steganographic files.
- Maintain the original file's quality and size.

## Tools Used
- **Steghide**: A powerful steganography tool included in Kali Linux.

## Usage
1. **Embedding Data:**
   ```bash
   steghide embed -cf <carrier_file> -ef <embedded_file>
   ```
   - `-cf`: Specifies the carrier file (e.g., an image or audio file).
   - `-ef`: Specifies the file to be hidden.

2. **Extracting Data:**
   ```bash
   steghide extract -sf <stego_file>
   ```
   - `-sf`: Specifies the steganographic file.

## Example
- Embedding a text file (`secret.txt`) into an image (`image.jpg`):
  ```bash
  steghide embed -cf image.jpg -ef secret.txt
  ```
- Extracting the hidden data from the steganographic image:
  ```bash
  steghide extract -sf image.jpg
  ```

## Notes
- Ensure Steghide is installed on your system. In Kali Linux, it is pre-installed.
- Use strong passphrases to secure your hidden data.

Happy steganography exploration!
