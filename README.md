# 🛒 Sistema de Cadastro de Produto com Django

Este é um sistema simples de cadastro de produtos desenvolvido com o framework Django. O projeto tem como objetivo demonstrar a criação de um CRUD básico com acesso ao painel administrativo.

## 📌 Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Edição e exclusão

## 🔐 Acesso ao Painel Administrativo

Para acessar o admin do Django:

* **Usuário:** admin
* **Senha:** [admin@admin.com](mailto:admin@admin.com)

Acesse em: `http://127.0.0.1:8000/admin/`

---

## ⚙️ Comandos Básicos do Django

Aqui estão os principais comandos utilizados no projeto:

### 🔹 Criar um novo projeto

```bash
django-admin startproject nome_do_projeto
```

Cria a estrutura inicial de um projeto Django.

### 🔹 Criar uma nova aplicação

```bash
python manage.py startapp nome_do_app
```

Cria uma nova aplicação dentro do projeto.

### 🔹 Aplicar migrações

```bash
python manage.py migrate
```

Aplica as migrações ao banco de dados, criando as tabelas necessárias.

### 🔹 Criar um superusuário

```bash
python manage.py createsuperuser
```

Cria um usuário administrador para acessar o painel admin.

### 🔹 Rodar o servidor

```bash
python manage.py runserver
```

Inicia o servidor local de desenvolvimento.

---

## 🗄️ Banco de Dados

Este projeto utiliza o banco de dados SQLite.

### 📖 Sobre o SQLite

O SQLite é um banco de dados relacional leve e que não necessita de servidor. Ele armazena todos os dados em um único arquivo no sistema, sendo ideal para:

* Projetos pequenos
* Desenvolvimento local
* Protótipos

### ✅ Vantagens

* Simples de configurar (já vem com o Django)
* Não precisa instalar nada adicional
* Ótimo para testes e aprendizado


---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd seu-repositorio
```

3. Execute as migrações:

```bash
python manage.py migrate
```

4. Rode o servidor:

```bash
python manage.py runserver
```

5. Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 📚 Tecnologias Utilizadas

* Python
* Django
* SQLite

---

