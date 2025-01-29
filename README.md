
# API RESTful com Docker e Testes Automatizados

Este projeto é uma API RESTful containerizada com Docker, conectando-se a um banco de dados também containerizado. Além disso, a API inclui testes automatizados com `pytest` e um seed inicial para criar um usuário padrão para testes.

## Tecnologias Utilizadas
- **Python** (FastAPI/Flask/Django Rest Framework, dependendo da sua escolha)
- **Docker** (para containerizar a aplicação e o banco de dados)
- **MariaDB** (banco de dados relacional)
- **Pytest** (para testes automatizados)
- **Alembic/Migrations** (para versionamento do banco, se aplicável)
- **Flasgger** (para documentação automática da API)

## Como Executar o Projeto

### 1. Clonar o repositório
```sh
 git clone https://github.com/seu-usuario/seu-repositorio.git
 cd seu-repositorio
```

### 2. Instalar as dependências
```sh
pip install -r requirements.txt
```
Isso garantirá que todas as bibliotecas necessárias estejam instaladas.

### 3. Criar e iniciar os containers Docker
```sh
docker-compose up
```
Isso criará a aplicação e o banco de dados.

### 4. Verificar se o Docker está funcionando corretamente
```sh
docker ps
```
Certifique-se de que os containers necessários estão rodando antes de continuar.

### 5. Executar a aplicação e criar o seed
```sh
python app.py
```
Isso garantirá que o seed inicial seja aplicado corretamente.

### 6. Acessar a documentação da API
Após iniciar a aplicação, a documentação gerada pelo Flasgger estará disponível em:
[http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

## Testes Automatizados
Para rodar os testes com `pytest`, execute:
```sh
pytest
```
Isso garantirá que a API esteja funcionando corretamente.

## Melhorias Implementadas
- Uso de Docker para containerização da API e banco de dados
- Testes automatizados com `pytest`
- Seed inicial para criação de um usuário padrão nos testes
- Documentação automática com Flasgger

## Créditos
Este projeto foi baseado no curso **crie apis rest com python e flask** do professor **Vitor Diogo Alves**, com melhorias adicionadas.

---

💡 **Sinta-se à vontade para contribuir ou sugerir melhorias!** 🚀
