# Simple Social

Uma rede social minimalista onde você pode postar fotos e vídeos, ver o feed de outros usuários e deletar os seus próprios posts. O backend é feito com FastAPI e o frontend com Streamlit. As mídias ficam hospedadas no ImageKit.

---

## Tecnologias

- **FastAPI** — API REST com autenticação JWT via `fastapi-users`
- **Streamlit** — interface web (frontend)
- **SQLite** com `aiosqlite` — banco de dados local (arquivo `test.db`)
- **ImageKit** — armazenamento e transformação de imagens/vídeos
- **Poetry** — gerenciamento de dependências

---

## Pré-requisitos

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation) instalado

---

## Configurando o ambiente

Clone o projeto e entre na pasta:

```bash
git clone <url-do-repositorio>
cd simple_social
```

Instale as dependências:

```bash
poetry install
```

Crie um arquivo `.env` na raiz do projeto (ou edite o existente) com as suas credenciais do ImageKit e uma chave secreta para o JWT:

```env
IMAGEKIT_PRIVATE_KEY=sua_private_key
IMAGEKIT_PUBLIC_KEY=sua_public_key
IMAGEKIT_URL=https://ik.imagekit.io/seu_id

SECRET_KEY=uma_chave_secreta_qualquer
```

> As credenciais do ImageKit você encontra no painel em [imagekit.io](https://imagekit.io). A `SECRET_KEY` pode ser qualquer string longa — ela é usada para assinar os tokens JWT.

---

## Rodando o projeto

O projeto tem dois processos que precisam rodar ao mesmo tempo: o backend e o frontend. Abra dois terminais.

**Terminal 1 — Backend (FastAPI):**

```bash
poetry run python main.py
```

A API vai subir em `http://localhost:8000`. Você pode acessar a documentação interativa em `http://localhost:8000/docs`.

**Terminal 2 — Frontend (Streamlit):**

```bash
poetry run streamlit run frontend.py
```

O Streamlit vai abrir automaticamente no navegador em `http://localhost:8501`.

---

## Usando o app

1. Acesse `http://localhost:8501`
2. Crie uma conta com email e senha (botão **Sign Up**)
3. Faça login
4. No menu lateral, escolha entre **Feed** (ver posts) ou **Upload** (postar mídia)
5. Para postar, selecione uma imagem ou vídeo, adicione uma legenda e clique em **Share**
6. Você pode deletar os seus próprios posts clicando no ícone 🗑️

---

## Estrutura do projeto

```
simple_social/
├── main.py          # ponto de entrada — sobe o uvicorn
├── frontend.py      # interface Streamlit
├── pyproject.toml   # dependências e config do Poetry
├── .env             # variáveis de ambiente (não sobe pro git)
└── src/
    ├── app.py       # rotas da API (upload, feed, delete)
    ├── db.py        # modelos do banco e configuração do SQLAlchemy
    ├── users.py     # autenticação JWT com fastapi-users
    ├── schemas.py   # schemas Pydantic
    └── images.py    # configuração do cliente ImageKit
```

---

## Observações

- O banco de dados é um arquivo SQLite (`test.db`) criado automaticamente na primeira vez que o backend sobe. Não precisa configurar nada.
- O backend precisa estar rodando para o frontend funcionar — ele faz requisições para `http://localhost:8000`.
- Formatos aceitos para upload: `png`, `jpg`, `jpeg`, `mp4`, `avi`, `mov`, `mkv`, `webm`.
- O token JWT expira em 1 hora. Depois disso é só fazer login de novo.