# Flask + Docker + CI

[![CI - Tests](https://github.com/VictorAlves-25/flask-docker-ci/actions/workflows/tests.yml/badge.svg)](https://github.com/VictorAlves-25/flask-docker-ci/actions/workflows/tests.yml)

Projeto desenvolvido para praticar conceitos de desenvolvimento web com **Python e Flask**, containerização com **Docker**, testes automatizados com **pytest** e integração contínua utilizando **GitHub Actions**.

## 🚀 Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## 📌 Sobre o projeto

A aplicação possui uma rota principal desenvolvida com Flask que retorna uma mensagem indicando que o serviço está funcionando corretamente.

O projeto também conta com:

- Containerização utilizando Docker
- Teste automatizado da rota principal
- Gerenciamento de dependências com `requirements.txt`
- Integração contínua com GitHub Actions
- Execução automatizada dos testes em pushes e Pull Requests
- Ambiente de testes utilizando Python 3.11

---

## 📂 Estrutura

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── app.py
├── test_app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## ▶️ Executando localmente

Clone o repositório:

```bash
git clone https://github.com/VictorAlves-25/flask-docker-ci.git
```

Entre na pasta:

```bash
cd flask-docker-ci
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

A aplicação ficará disponível em:

```text
http://localhost:5000
```

---

## 🐳 Executando com Docker

Construa a imagem:

```bash
docker build -t flask-app .
```

Execute o container:

```bash
docker run -p 5000:5000 flask-app
```

Depois acesse:

```text
http://localhost:5000
```

---

## 🧪 Testes

Os testes automatizados são executados utilizando **pytest**.

Para executar localmente:

```bash
pytest
```

O teste atual verifica se:

- A rota `/` responde corretamente
- O status HTTP retornado é `200`
- O conteúdo esperado é retornado pela aplicação

---

## ⚙️ Integração contínua

O projeto possui um workflow de integração contínua configurado com **GitHub Actions**.

Os testes são executados automaticamente quando:

- Um novo `push` é enviado para a branch `main`
- Um Pull Request é aberto ou atualizado para a branch `main`

Durante a execução, o GitHub Actions:

1. Prepara um ambiente Linux
2. Faz o checkout do repositório
3. Configura o Python 3.11
4. Utiliza cache das dependências do `pip`
5. Instala as dependências do projeto
6. Executa os testes com `pytest`

O status do workflow pode ser acompanhado pelo badge exibido no início deste README.

---

## 🎯 Objetivo

Este projeto faz parte dos meus estudos práticos em desenvolvimento de software e tem como objetivo exercitar conceitos de:

- Python
- Desenvolvimento web com Flask
- Testes automatizados
- Docker
- Git e GitHub
- GitHub Actions
- Integração contínua
- Boas práticas de desenvolvimento

---

## 👨‍💻 Autor

**João Victor Alves da Silva**

[![GitHub](https://img.shields.io/badge/GitHub-VictorAlves--25-181717?style=for-the-badge&logo=github)](https://github.com/VictorAlves-25)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-João_Victor-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/joao-silva-a7720b1b8)
