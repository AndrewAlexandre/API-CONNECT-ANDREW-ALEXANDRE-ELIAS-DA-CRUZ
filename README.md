# ANDREW ALEXANDRE ELIAS DA CRUZ

# ATIVIDADE 2 DESENVOLVIMENTO BACK-END

# API Connect — Gerenciamento de Usuários

API REST desenvolvida em Python com Flask para gerenciamento de usuários, como parte da atividade acadêmica de Back-End.

## 1. Descrição

O projeto consiste em uma API REST para gerenciamento de usuários. A aplicação permite listar, buscar, cadastrar, atualizar e excluir usuários por meio de requisições HTTP.

Os dados são trabalhados no formato JSON e armazenados temporariamente em uma lista em memória. Dessa forma, os dados permanecem disponíveis enquanto o servidor estiver em execução, mas são perdidos quando a aplicação é encerrada.

A aplicação foi organizada em arquivos separados para facilitar a manutenção e a compreensão do código, dividindo a inicialização da aplicação, as rotas e os dados e regras de validação.

## 2. Tecnologias utilizadas

- Python 3
- Flask
- HTTP/REST
- JSON
- Visual Studio Code
- Postman para testes das requisições
- Git e GitHub para versionamento e compartilhamento do projeto

## 3. Estrutura do projeto

ATIVIDADE 2 BACKEND/
├── venv/
├── .gitignore
├── app.py
├── routes.py
├── dados.py
├── requirements.txt
└── README.md


### app.py

Arquivo responsável pela inicialização da aplicação Flask e pelo registro das rotas da API.

### routes.py

Arquivo responsável pelas rotas e pelos controladores das operações HTTP da API, incluindo GET, POST, PUT, PATCH e DELETE.

### dados.py

Arquivo responsável pelos dados dos usuários armazenados em memória, pela validação dos dados recebidos e pela geração dos próximos IDs.

### requirements.txt

Arquivo que registra as dependências Python utilizadas pelo projeto.

### README.md

Arquivo de documentação do projeto, contendo informações sobre a API, tecnologias utilizadas, instalação, execução, rotas e exemplos de requisições.

### venv/

Ambiente virtual utilizado para manter as dependências do projeto isoladas. Esse diretório não deve ser enviado ao GitHub.

### .gitignore

Arquivo utilizado para indicar arquivos e diretórios que não devem ser enviados para o controle de versão, como o ambiente virtual e arquivos temporários do Python.

## 4. Inicialização do projeto

O ambiente virtual foi criado utilizando o seguinte comando:

powershell
python -m venv venv


Para ativar o ambiente virtual no PowerShell:

powershell
.\venv\Scripts\Activate.ps1


Com o ambiente virtual ativado, o Flask foi instalado utilizando:

powershell
pip install flask


As dependências instaladas foram registradas no arquivo requirements.txt através do comando:

powershell
pip freeze > requirements.txt


## 5. Execução da aplicação

Com o ambiente virtual ativado, a API pode ser iniciada utilizando:

powershell
python app.py


Após a inicialização, o servidor fica disponível localmente no endereço:
http://127.0.0.1:5000


## 6. Endpoints da API

| Método | Endpoint | Descrição | Status de sucesso |
|---|---|---|---|
| GET | /usuarios | Lista todos os usuários | 200 |
| GET | /usuarios/<id> | Busca um usuário pelo ID | 200 |
| POST | /usuarios | Cadastra um novo usuário | 201 |
| PUT | /usuarios/<id> | Atualiza completamente um usuário | 200 |
| PATCH | /usuarios/<id> | Atualiza parcialmente um usuário | 200 |
| DELETE | /usuarios/<id> | Exclui um usuário | 200 |

## 7. Validação dos dados

A API possui validações para garantir a integridade dos dados recebidos nas operações de cadastro e atualização.

No POST e no PUT, os campos nome, email e idade são obrigatórios.

O campo nome deve ser um texto e não pode estar vazio.

O campo email deve ser um texto não vazio e deve conter o caractere @. A aplicação também verifica se o @ não está no início ou no final do endereço informado.

O campo idade deve ser um número inteiro maior ou igual a zero.

No PATCH, é possível alterar somente os campos desejados. Os campos que não forem enviados permanecem inalterados.

A API também verifica se os campos enviados no PATCH são permitidos.

## 8. Códigos de status HTTP

A API utiliza códigos de status HTTP para indicar o resultado das operações:

- 200 OK — operação realizada com sucesso.
- 201 Created — novo usuário criado com sucesso.
- 400 Bad Request — dados ausentes ou inválidos.
- 404 Not Found — usuário não encontrado.

As respostas de erro são retornadas em formato JSON, utilizando a chave "erro" para informar o problema encontrado.

## 9. Exemplos de requisições

### Listar usuários

http
GET /usuarios


### Buscar usuário por ID

http
GET /usuarios/1


### Cadastrar usuário

http
POST /usuarios


Corpo da requisição:

json
{
    "nome": "Carlos",
    "email": "carlos@gmail.com",
    "idade": 25
}


Resposta esperada: 201 Created.

### Atualizar completamente um usuário

http
PUT /usuarios/1


Corpo da requisição:

json
{
    "nome": "Andrew Alexandre Elias Da Cruz",
    "email": "andrew.novo@gmail.com",
    "idade": 24
}


Resposta esperada: 200 OK.

### Atualizar parcialmente um usuário

http
PATCH /usuarios/1


Corpo da requisição:

json
{
    "email": "andrew.novo@gmail.com"
}


Nesse caso, somente o email será alterado.

### Excluir usuário

http
DELETE /usuarios/1


Resposta esperada: 200 OK.

## 10. Geração dos IDs

Os usuários são armazenados em uma lista em memória no arquivo dados.py.

Para cadastrar um novo usuário, a aplicação identifica o maior ID existente e adiciona 1 ao seu valor para gerar o próximo identificador.

Dessa forma, não é necessário informar manualmente o ID durante o cadastro.

## 11. Idempotência

A operação PUT é idempotente em relação ao estado do recurso, pois enviar repetidamente os mesmos dados para o mesmo usuário mantém o recurso no mesmo estado.

A operação DELETE também possui comportamento idempotente em relação ao estado do recurso: depois que o usuário é removido, ele permanece inexistente. Uma nova tentativa de exclusão, entretanto, retorna 404 porque o usuário não foi encontrado.

A operação POST não é idempotente, pois o envio repetido da mesma requisição pode criar novos usuários.

## 12. Testes com Postman

As requisições da API foram testadas utilizando o Postman.

Foram realizados testes para verificar:

1. Listagem dos usuários com GET.
2. Busca de usuário existente por ID.
3. Busca de usuário inexistente.
4. Cadastro de usuário com dados válidos.
5. Cadastro sem campos obrigatórios.
6. Cadastro com nome ou email vazio.
7. Cadastro com email inválido.
8. Cadastro com idade inválida.
9. Atualização completa com PUT.
10. Atualização parcial com PATCH.
11. Exclusão de usuário com DELETE.
12. Tentativa de exclusão de usuário inexistente.

## 13. Persistência dos dados

Para esta atividade, não foi utilizado um banco de dados. A persistência foi simulada utilizando uma lista Python armazenada na memória do servidor.

Essa abordagem permite testar as operações de gerenciamento de usuários sem adicionar a complexidade de um banco de dados ao projeto.

Como consequência, os dados cadastrados ou modificados são perdidos quando o servidor é encerrado.

## 14. Versionamento

O projeto utiliza Git para controle de versão e GitHub para armazenamento e compartilhamento do código-fonte.

O arquivo .gitignore impede que arquivos e diretórios desnecessários, como o ambiente virtual venv, sejam enviados ao repositório.

O arquivo requirements.txt registra as dependências utilizadas pela aplicação, permitindo identificar os pacotes necessários para executar o projeto.



