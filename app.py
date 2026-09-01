"""API para gerenciamento de usuários.

Este módulo expõe endpoints para listar, buscar, criar, atualizar e
excluir usuários em memória, seguindo uma estrutura simples de API REST.
"""

from flask import Flask, request

app = Flask(__name__)

# Persistência simulada em memória para armazenar os usuários.
usuarios = [
    {
        "id": 1,
        "nome": "Andrew Alexandre Elias Da Cruz",
        "email": "andrewalexandre232@gmail.com",
        "idade": 24,
    },
    {
        "id": 2,
        "nome": "Bianca dos Santos Ribeiro",
        "email": "naolembro@gmail.com",
        "idade": 23,
    },
    {
        "id": 3,
        "nome": "Elizabeth Ferreira Elias",
        "email": "naotenhoideia@gmail.com",
        "idade": 43,
    },
]


def validar_dados_usuario(dados):
    """Valida os dados completos de um usuário."""
    if not isinstance(dados, dict) or not dados:
        return "O corpo da requisição é obrigatório"

    for campo in ("nome", "email", "idade"):
        if campo not in dados:
            return f"O campo '{campo}' é obrigatório"

    if not isinstance(dados["nome"], str) or not dados["nome"].strip():
        return "O nome deve ser um texto não vazio"

    if not isinstance(dados["email"], str) or not dados["email"].strip():
        return "O email deve ser um texto não vazio"

    email = dados["email"].strip()
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return "O email deve ser válido e conter @"

    if not isinstance(dados["idade"], int) or isinstance(dados["idade"], bool):
        return "A idade deve ser um número inteiro"

    if dados["idade"] < 0:
        return "A idade não pode ser negativa"

    return None


def proximo_id():
    """Gera um ID maior que todos os IDs existentes."""
    return max((usuario["id"] for usuario in usuarios), default=0) + 1


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    return usuarios, 200


@app.route("/usuario/<int:id>", methods=["GET"])
def buscar_usuario(id):
    """Busca um usuário específico pelo ID."""
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario, 200

    return {"erro": "Usuário não encontrado"}, 404


@app.route("/usuario", methods=["POST"])
def criar_usuario():
    """Cria um novo usuário com os dados fornecidos."""
    dados = request.get_json(silent=True)
    erro = validar_dados_usuario(dados)

    if erro:
        return {"erro": erro}, 400

    novo_usuario = {
        "id": proximo_id(),
        "nome": dados["nome"].strip(),
        "email": dados["email"].strip(),
        "idade": dados["idade"],
    }

    usuarios.append(novo_usuario)

    return novo_usuario, 201


@app.route("/usuario/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    """Atualiza todos os dados de um usuário existente."""
    dados = request.get_json(silent=True)
    erro = validar_dados_usuario(dados)

    if erro:
        return {"erro": erro}, 400

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = dados["nome"].strip()
            usuario["email"] = dados["email"].strip()
            usuario["idade"] = dados["idade"]

            return usuario, 200

    return {"erro": "Usuário não encontrado"}, 404


@app.route("/usuario/<int:id>", methods=["PATCH"])
def atualizar_parcial_usuario(id):
    """Atualiza apenas os campos enviados para um usuário específico."""
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict) or not dados:
        return {"erro": "O corpo da requisição é obrigatório"}, 400

    campos_permitidos = {"nome", "email", "idade"}
    campos_invalidos = set(dados) - campos_permitidos

    if campos_invalidos:
        return {
            "erro": "Campo(s) não permitido(s)",
            "campos": list(campos_invalidos),
        }, 400

    for usuario in usuarios:
        if usuario["id"] == id:
            if "nome" in dados:
                if (
                    not isinstance(dados["nome"], str)
                    or not dados["nome"].strip()
                ):
                    return {
                        "erro": "O nome deve ser um texto não vazio"
                    }, 400

                usuario["nome"] = dados["nome"].strip()

            if "email" in dados:
                if (
                    not isinstance(dados["email"], str)
                    or not dados["email"].strip()
                ):
                    return {
                        "erro": "O email deve ser um texto não vazio"
                    }, 400

                email = dados["email"].strip()
                if (
                    "@" not in email
                    or email.startswith("@")
                    or email.endswith("@")
                ):
                    return {
                        "erro": "O email deve ser válido e conter @"
                    }, 400

                usuario["email"] = email

            if "idade" in dados:
                if (
                    not isinstance(dados["idade"], int)
                    or isinstance(dados["idade"], bool)
                ):
                    return {
                        "erro": "A idade deve ser um número inteiro"
                    }, 400

                if dados["idade"] < 0:
                    return {
                        "erro": "A idade não pode ser negativa"
                    }, 400

                usuario["idade"] = dados["idade"]

            return usuario, 200

    return {"erro": "Usuário não encontrado"}, 404


@app.route("/usuario/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    """Remove um usuário pelo ID informado."""
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário excluído com sucesso"}, 200

    return {"erro": "Usuário não encontrado"}, 404


if __name__ == "__main__":
    # Executa o servidor Flask em modo de depuração.
    app.run(debug=True)