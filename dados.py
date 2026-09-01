"""Dados e regras de validação da API."""

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
    return max(
        (usuario["id"] for usuario in usuarios),
        default=0
    ) + 1