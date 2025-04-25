FROM python:3.13-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-6 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Diretório da aplicação
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para rodar a aplicação
CMD ["python", "main.py"]
