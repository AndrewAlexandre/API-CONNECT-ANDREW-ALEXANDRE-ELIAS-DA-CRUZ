"""Aplicação principal da API de gerenciamento de usuários."""

from flask import Flask

from routes import usuario_bp


app = Flask(__name__)

app.register_blueprint(usuario_bp)


if __name__ == "__main__":
    app.run(debug=True)