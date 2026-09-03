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
