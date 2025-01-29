from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurações da aplicação
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Verifique se este valor é carregado corretamente
jwt = JWTManager(app)

@app.route('/token', methods=['GET'])
def generate_token():
    token = create_access_token(identity="usuario_id")
    return {"token": token}

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return {"message": f"Bem-vindo, {current_user}!"}

if __name__ == '__main__':
    print(f"JWT_SECRET_KEY usado: {app.config['JWT_SECRET_KEY']}")  # Certifique-se que o valor está correto
    app.run(debug=True)
