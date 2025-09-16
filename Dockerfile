# Imagem base
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar requirements.txt e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY app ./app

# Expor a porta que o Flask vai usar
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "app/main.py"]

