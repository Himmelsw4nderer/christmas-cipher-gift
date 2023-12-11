"""
app.py

A simple Flask web application for Caesar cipher encryption and decryption.
"""
from flask import Flask, render_template, request
import urllib.parse
import qrcode
import os


app = Flask(__name__, static_folder='images')

def caesar_decrypt(text, key):
    """
    Decrypts the given text using the Caesar cipher.

    Args:
        text (str): The text to be decrypted.
        key (str): The decryption key.

    Returns:
        str: The decrypted text.
    """
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length]) - ord('a')  # Adjust if the key contains uppercase letters
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

def caesar_encrypt(text, key):
    """
    Decrypts the given text using the Caesar cipher.

    Args:
        text (str): The text to be decrypted.
        key (str): The decryption key.

    Returns:
        str: The decrypted text.
    """
    result = ""
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length]) - ord('a')  # Adjust if the key contains uppercase letters
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def generate_qr_code(data):
    """
    Generates a QR code for the given data.

    Args:
        data (str): The data to be encoded in the QR code.

    Returns:
        qrcode.QRCode.image: The generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def generate_url(text, key):
    """
    Generates a URL with Caesar encryption using a key.

    Args:
        text (str): The text to be encrypted and included in the URL.
        key (str): The encryption key.

    Returns:
        str: The generated URL.
    """
    encrypted_text = caesar_encrypt(text, key)
    url_encoded_text = urllib.parse.quote(encrypted_text)
    ip_address = os.environ.get("IP", "127.0.0.1")
    url = f"http://{ip_address}:5000/encrypt?q={url_encoded_text}"
    return url


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles requests to the index route.

    Returns:
        str: The rendered HTML template.
    """
    key = request.args.get('key', default='')
    encrypted_text = request.args.get('q', default='')
    decrypted_text = ""

    if key and encrypted_text:
        decrypted_text = caesar_decrypt(encrypted_text, key)

    return render_template('index.html', key=key, encrypted_text=encrypted_text, decrypted_text=decrypted_text)


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    Handles requests to the encrypt route.

    Returns:
        str: The rendered HTML template.
    """
    key = request.args.get('key', default='')
    plain_text = request.args.get('q', default='')
    link_text = ""
    qr_code = False
   
    
    if key and plain_text:
        link_text = generate_url(plain_text, key)
        qr_code = generate_qr_code(link_text)
        qr_code.save('images/qr_code.png')

    return render_template('encrypt.html', link_text=link_text, plain_text=plain_text, key=key, qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)
