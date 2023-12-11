# Christmas Cipher Gift 🎁🔐

## Overview

This festive Flask web application aims to add an element of surprise and excitement to Christmas gifting. Instead of traditional gift tags, spice up your presents with a fun and interactive twist using the Christmas Cipher Gift!

## How It Works

1. **Encryption**: Enter a unique encryption key and a personalized message for your gift recipient [/encrypt](http://127.0.0.1:5000/encrypt).
2. **QR Code**: The application generates a QR code for the encrypted message.
3. **Gift Tag**: Print the QR code and attach it to your gift as a unique and interactive gift tag.

On Christmas day, your recipient can use the web app to decrypt the message, unveiling the heartfelt note you've hidden within the cipher.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Himmelsw4nderer/CesarChristmas.git
   cd christmas-cipher-gift
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Open the app in your browser at http://127.0.0.1:5000.

## Docker Deployment

1. Build the Docker Image

   ```bash
   docker build -t christmas-cipher .
   ```

2. Run the Docker Container
   Replace <YOUR_LOCAL_IP> with your local machine's IP address.

   ```bash
   docker run -e IP=<YOUR_LOCAL_IP> -p 5000:5000 christmas-cipher
   ```

## Environment Variables

- IP: The IP address to be used in the generated URL.

## Credits

- Application developed by Nils Baxheinrich
- Image source: [Karosieben on Pixabay](https://pixabay.com/de/photos/weihnachten-geschenk-dekoration-1786558/).

License

This project is licensed under the MIT License - see the LICENSE file for details.
