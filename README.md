# Sistema de Gerenciamento de Galerias de Fotografia

## Sobre o Projeto

O **Sistema de Gerenciamento de Galerias de Fotografia** é uma solução personalizada desenvolvida para facilitar a administração de clientes e galerias fotográficas. Criado utilizando o framework Django e orquestrado com Docker, o sistema é robusto, escalável e oferece funcionalidades completas para gestão de clientes e hospedagem de galerias.

---

## Funcionalidades Principais

- **Gerenciamento de Galerias**: Criação e administração das galerias e planos de hospedagem.
- **Gerenciamento de Clientes**: Registro e administração de clientes.
- **Integração de Serviços**: 
  - Banco de dados PostgreSQL para armazenamento seguro de dados.
  - Redis para otimização de performance com cache.
  - Nginx para servir a aplicação e arquivos estáticos.

---

## Tecnologias Utilizadas

- **Backend**: Django (Python)
- **Banco de Dados**: PostgreSQL
- **Cache**: Redis
- **Orquestração**: Docker e Docker Compose
- **Servidor Web**: Nginx

---

## Estrutura do Projeto

A estrutura do projeto segue o seguinte padrão:

```
SYSTEM_Administracao-de-galerias/
|— adminer/       # Configurações do Adminer
|— django/        # Aplicação Django
|— nginx/         # Configurações do Nginx
|— postgres/      # Dados e configurações do PostgreSQL
|— redis/         # Configurações do Redis
|— docker-compose.yml  # Configuração do Docker Compose
```

---

## Requisitos

- **Docker**
- **Docker Compose**
- **Git**

Certifique-se de que essas ferramentas estejam instaladas em seu sistema antes de prosseguir.

---

## Como Instalar e Rodar o Projeto

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/MuzNocci/SYSTEM_Administracao-de-galerias.git
   cd SYSTEM_Administracao-de-galerias
   ```

2. **Inicie os Contêineres**:

   ```bash
   docker-compose up -d
   ```

   Esse comando inicializa todos os contêineres definidos no `docker-compose.yml`.

3. **Acesse a Aplicação**:

   Abra o navegador e acesse:

   - **Aplicação Web**: `http://localhost`
   - **Adminer** (gerenciamento do banco de dados): `http://localhost:8080`

---

## Personalizações e Configurações Adicionais

- **Variáveis de Ambiente**:

  Você pode configurar as variáveis de ambiente no arquivo `.env` para ajustar os parâmetros do banco de dados, cache e outros serviços.

- **Admin do Django**:

  Para acessar o painel administrativo do Django, crie um superusuário:

  ```bash
  docker exec -it <nome-do-contêiner-django> python manage.py createsuperuser
  ```

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade ou correção:

   ```bash
   git checkout -b minha-feature
   ```

3. Submeta um pull request descrevendo suas alterações.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Contato

Desenvolvido por **Müller Nocciolli**. Entre em contato pelo [LinkedIn](https://www.linkedin.com) ou envie um e-mail para **mullernocciolli@example.com**.