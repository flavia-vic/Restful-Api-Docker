from users.model import UsersModel  # Importa apenas o modelo de usuários

def create_user():
    # Verifica se o usuário já existe
    if not UsersModel.query.filter_by(email="admin@gmail.com").first():
        user = UsersModel(
            email="admin@gmail.com",
            password="admin123456"  # A senha será automaticamente criptografada no modelo
        )
        user.save()  # Método save que você criou no modelo para adicionar e salvar no banco
        print("Usuário admin criado com sucesso!")
    else:
        print("Usuário admin já existe.")