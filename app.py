import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from db import db
from flasgger import Swagger
from dotenv import load_dotenv
from flask_cors import CORS
from seeds.run_seeds import run_all_seeds 




from purchase_orders.resources import PurchaseOrders, PurchaseOrderById
from purchase_orders_items.resources import PurchaseOrdersItems
from users.resources import UserCreation, UserLogin

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    

    # Configurações do app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Inicialização de extensões
    db.init_app(app)
    Migrate(app, db)
    jwt = JWTManager(app)

    # Configuração do Flasgger
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "API de Gestão de Pedidos",
            "description": "Documentação dos endpoints da API.",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": ["http"]
    })


    # Registro de recursos
    api.add_resource(PurchaseOrders, '/purchase_orders')
    api.add_resource(PurchaseOrderById, '/purchase_orders/<int:id>')
    api.add_resource(PurchaseOrdersItems, '/purchase_orders/<int:id>/items')
    api.add_resource(UserCreation, '/users')
    api.add_resource(UserLogin, '/login')

    # JWT Handlers
    @jwt.invalid_token_loader
    def invalid_jwt_callback(error):
        print(f"Token inválido: {error}")
        return {"message": "Token de acesso inválido"}, 401

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return {"message": "O token está expirado"}, 401

    # Criar tabelas no primeiro request
    @app.before_request
    def create_tables():
        db.create_all()  # Cria as tabelas no banco de dados
        print("Tabelas e seeds criadas com sucesso!")




    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Cria as tabelas
        run_all_seeds()
    app.run(debug=True, host="0.0.0.0")

