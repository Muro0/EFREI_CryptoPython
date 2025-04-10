from cryptography.fernet import Fernet, InvalidToken
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# ➕ Nouvelle route : chiffrement AVEC clé fournie
@app.route('/encrypt/<key>/<valeur>')
def encrypt_with_key(key, valeur):
    try:
        fernet = Fernet(key.encode())
        token = fernet.encrypt(valeur.encode())
        return f"Valeur encryptée avec votre clé : {token.decode()}"
    except Exception as e:
        return f"Erreur de chiffrement : {str(e)}"

# ➕ Nouvelle route : déchiffrement AVEC clé fournie
@app.route('/decrypt/<key>/<valeur>')
def decrypt_with_key(key, valeur):
    try:
        fernet = Fernet(key.encode())
        decrypted = fernet.decrypt(valeur.encode())
        return f"Valeur décryptée avec votre clé : {decrypted.decode()}"
    except InvalidToken:
        return "Clé invalide ou valeur corrompue."
    except Exception as e:
        return f"Erreur de déchiffrement : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
