"""Rotas da API de gerenciamento de usuários."""

from flask import Blueprint, request

from dados import usuarios, validar_dados_usuario, proximo_id


usuario_bp = Blueprint("usuario", __name__)


@usuario_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    return usuarios, 200


@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    """Busca um usuário específico pelo ID."""
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario, 200

    return {"erro": "Usuário não encontrado"}, 404


@usuario_bp.route("/usuarios", methods=["POST"])
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


@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
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


@usuario_bp.route("/usuarios/<int:id>", methods=["PATCH"])
def atualizar_parcial_usuario(id):
    """Atualiza apenas os campos enviados."""
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


@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    """Remove um usuário pelo ID informado."""
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)

            return {
                "mensagem": "Usuário excluído com sucesso"
            }, 200

    return {"erro": "Usuário não encontrado"}, 404