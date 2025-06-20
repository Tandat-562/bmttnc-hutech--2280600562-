import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ex01')))
from flask import Flask, render_template, request
from ex01.cipher.caesar.caesar_cipher import CaesarCipher
app = Flask(__name__)

# Route cho trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Route cho trang Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Route xử lý mã hóa Caesar
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)

    return f"""
    <h3>Kết quả mã hóa:</h3>
    <p><strong>Text:</strong> {text}</p>
    <p><strong>Key:</strong> {key}</p>
    <p><strong>Encrypted Text:</strong> {encrypted_text}</p>
    <a href="/caesar">Quay lại</a>
    """

# Route xử lý giải mã Caesar
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)

    return f"""
    <h3>Kết quả giải mã:</h3>
    <p><strong>Text:</strong> {text}</p>
    <p><strong>Key:</strong> {key}</p>
    <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
    <a href="/caesar">Quay lại</a>
    """

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5850, debug=True)
