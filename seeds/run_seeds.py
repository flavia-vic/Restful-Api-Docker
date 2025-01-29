from seeds.seed_user import create_user  # Certifique-se de importar corretamente

def run_all_seeds():
    # Rodando as seeds, como a criação do usuário admin
    create_user()
    print("Seeds rodadas com sucesso!")
