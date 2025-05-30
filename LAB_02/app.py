from flask import Flask, render_template, request, json
from caesar_cipher import CaesarCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    # Get text and key from the form
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    # Initialize CaesarCipher and encrypt
    caesar_cipher = CaesarCipher() # Corrected: instantiate the class
    encrypted_text = caesar_cipher.encrypt_text(text, key) # Corrected: call method on instance

    # Return the result (you might want to render a template here instead)
    return f"Plain Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    # Get text and key from the form
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    # Initialize CaesarCipher and decrypt
    caesar_cipher = CaesarCipher() # Corrected: instantiate the class
    decrypted_text = caesar_cipher.decrypt_text(text, key) # Corrected: call method on instance

    # Return the result (you might want to render a template here instead)
    return f"Cipher Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True) # Changed port to 5050 for common practice                                                                                                                                                              