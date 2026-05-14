# Dockerfile para o app FastAPI
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Expor porta onde o app irá rodar
EXPOSE 8000

# Comando padrão para iniciar o servidor
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# comando:
    # docker build -t pokemon-app .
    # docker run -p 8000:8000 pokemon-app