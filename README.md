# FakePinterest

### Objetivo:

Criação de site replicando Pinterest.

### Características:

Criação de autenticação de login, base de dados para feed principal e upload de imagens.

### Ferramentas:

- Python
  - Flask
- Html
- Css

### Arquivos Explicação:

- main.py -> Arquivo principal, voltado para executar o site.
- criar_banco_dados.py -> Arquivo para criação de um banco de dados para salvamento das imagens e usuários.
- ./fakepinterest -> Pasta de armazenamento do projeto do site.
  - Pasta static -> Pasta para configurações CSS dos arquivos HTMLs e para guardar as imagens staticas que estarão presentes no site, como posts de usuários.
  - Pasta templates -> Pasta para guardar as paginas de HTML (frontend).
  - __init__.py -> Arquivo que quando executado irá iniciar o projeto, carregando as configurações iniciais do site, do banco de dados, e o gerenciamento de login.
  - forms.py -> Arquivo para criar os formulários de login, criação de conta e upload de imagens que estarão presentes dentro do site (backend).
  - models.py -> Arquivo criado para estruturar como os dados dos usuários e das imagens serão armazenadas dentro do banco de dados (backend).
  - routes.py -> Arquivo para gerir o que irá em cada página HTML da pasta templates e como funcionarão (backend).