# Blog de Filmes

Bem-vindo ao Blog de Filmes! Este é um projeto que permite aos usuários postar suas opiniões sobre os filmes que assistiram.

## Descrição do Projeto

O Blog de Filmes é uma plataforma onde os usuários podem se cadastrar, fazer login e postar suas opiniões sobre os filmes que assistiram. Eles podem compartilhar suas críticas, avaliações e recomendações com outros usuários da plataforma.

Além disso, os usuários também podem visualizar as postagens de outros usuários, comentar nelas e interagir com a comunidade de cinéfilos.

## Funcionalidades Principais

- Cadastro de usuários: os usuários podem se cadastrar na plataforma para criar uma conta.
- Autenticação: os usuários podem fazer login e logout de suas contas.
- Postagem de Opiniões: os usuários podem postar suas opiniões sobre os filmes que assistiram, incluindo título, descrição e avaliação.
- Visualização de Postagens: os usuários podem visualizar as postagens de outros usuários.
- Comentários: os usuários podem comentar nas postagens de outros usuários para compartilhar suas opiniões e iniciar discussões.
- Integração com API de Filmes: o sistema pode integrar-se a uma API de filmes para obter informações sobre os filmes mencionados nas postagens dos usuários.

## Tecnologias Utilizadas

- **Django**: Framework web em Python usado para desenvolver a aplicação.
- **HTML/CSS**: Linguagens de marcação e estilo para criar a interface do usuário.
- **Bootstrap**: Framework front-end para design responsivo e componentes de interface do usuário.
- **SQLite**: Banco de dados relacional para armazenar informações de usuário e postagem.

# Objetivo da Aplicação
O objetivo deste aplicativo é permitir que os usuários compartilhem suas opiniões e resenhas sobre os filmes que assistiram. Ele oferece uma plataforma onde os usuários podem escrever posts, discutir filmes, ver as opiniões de outros usuários e descobrir novos filmes para assistir.

# Justificação Técnica da Escolha da Framework
A escolha da framework Django foi baseada em vários fatores:

Rápido Desenvolvimento: Django oferece um conjunto abrangente de ferramentas e bibliotecas que facilitam o desenvolvimento rápido de aplicativos da web.
Segurança: Django possui recursos de segurança incorporados, como prevenção contra injeção de SQL, proteção contra CSRF e autenticação de usuário integrada.
Documentação Completa: A documentação oficial do Django é extensa e bem organizada, facilitando o aprendizado e a resolução de problemas.
Comunidade Ativa: Django possui uma comunidade de desenvolvedores ativa e de suporte, o que significa que é fácil encontrar ajuda e recursos adicionais online.
Escalabilidade: Django é altamente escalável e pode lidar com grandes volumes de tráfego e dados, tornando-o adequado para projetos em crescimento.

## Instalação e Configuração

1. Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/blog_movies.git
```

2. Instale as dependências do Python:

```bash
pip install poetry
pip install django
```

3. Execute as migrações do Django:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Inicie o servidor de desenvolvimento:

```bash
docker-compose build
docker-composer up
ou
python manage.py runserver
```

5. Acesse o aplicativo em seu navegador em `http://localhost:8000`.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor abra uma issue para discutir as mudanças propostas ou envie uma pull request.

## Autores

- Jessiellen Souza

## Licença

Este projeto é licenciado sob a Licença [MIT](https://opensource.org/licenses/MIT).

---

Sinta-se à vontade para personalizar este README de acordo com as especificidades do seu projeto e adicionar mais detalhes conforme necessário.
