# BASE_to_projects


## Descrição

O projeto **BASE_to_projects** é uma estrutura inicial para projetos desenvolvidos com o framework Django, configurada para ser executada em contêineres Docker. Esta base visa agilizar o início do desenvolvimento, fornecendo uma configuração prévia que inclui serviços comumente utilizados em aplicações web.


## Funcionalidades

- **Integração com Docker:** Facilita a criação e gerenciamento de ambientes isolados para a aplicação.
- **Serviços pré-configurados:**
  - **PostgreSQL:** Banco de dados relacional para armazenamento de dados.
  - **Redis:** Armazenamento em memória utilizado para cache e filas.
  - **Nginx:** Servidor web para servir a aplicação e arquivos estáticos.
  - **Adminer:** Interface gráfica para gerenciamento do banco de dados.
- **Estrutura Django pronta para desenvolvimento:** Inclui configurações iniciais para iniciar o desenvolvimento de imediato.


## Requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados em seu ambiente:

- **Docker:** [Instalação do Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Instalação do Docker Compose](https://docs.docker.com/compose/install/)


## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. **Clone o repositório:**

\`\`\`bash
git clone https://github.com/MuzNocci/BASE_to_projects.git
\`\`\`

2. **Navegue até o diretório do projeto:**

Para acessar o diretório do projeto, execute o comando abaixo:

\`\`\`bash
cd BASE_to_projects
\`\`\`

3. **Configuração:**
Antes de executar o projeto, configure as variáveis de ambiente necessárias:

4. **Editar o arquivo \`.env_example\` para \`.env\`:**

Edite o arquivo \`.env\` e defina os seguintes valores:

*   \`DJANGO_SECRET_KEY\`: Chave secreta para a aplicação Django.
*   \`POSTGRES_DB\`: Nome do banco de dados PostgreSQL.
*   \`POSTGRES_USER\`: Usuário do banco de dados.
*   \`POSTGRES_PASSWORD\`: Senha do banco de dados.
*   E os outros valores conforme necessário.

5. **Editar o arquivo \`.init-database.sh_example\` para \`init-database.sh\`:**

Substitua usuario, senhadousario e bancodedados, conforme necessário e de acordo com os dados contidos no arquivo "docker-compose.yml".

6. **Iniciar os contêineres em segundo plano:**

Utilize o seguinte comando para iniciar os contêineres em segundo plano:

\`\`\`bash
docker-compose up --build -d
\`\`\`

7. **Parar os contêineres:**

Para parar os contêineres, utilize:

\`\`\`bash
docker-compose down
\`\`\`


## Uso

Após a configuração, acesse a aplicação em \`http://0.0.0.0:8000\`.


## Contribuição

Contribuições são bem-vindas!


### Como contribuir

1.  Faça um fork deste repositório.
2.  Crie uma nova branch para sua feature:

\`\`\`bash
git checkout -b feature/nova-feature
\`\`\`

3.  Faça o commit das suas alterações:

\`\`\`bash
git commit -m 'Adiciona nova feature'
\`\`\`

4.  Faça o push para a branch criada:

\`\`\`bash
git push origin feature/nova-feature
\`\`\`

5.  Abra um Pull Request para o repositório original.


## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo \`LICENSE\` para mais detalhes.


## Contato

Para mais informações, entre em contato:

*   Nome: \[Müller Nocciolli]
*   Email: \[muller.nocciolli@gmail.com]
*   LinkedIn: \[https://www.linkedin.com/in/m%C3%BCller-nocciolli/]