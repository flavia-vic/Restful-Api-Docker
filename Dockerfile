# Use uma imagem base para Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos para o contêiner
COPY . .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta da aplicação
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
