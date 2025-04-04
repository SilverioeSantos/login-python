FROM python:3

# Define o diretório de trabalho
WORKDIR /usr/src/app

# Atualiza os pacotes e instala dependências para X11 e Tkinter
RUN apt-get update && apt-get install -y \
    x11-apps \
    x11-utils \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências e instala os pacotes Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos para dentro do container
COPY . .

# Define a variável DISPLAY para rodar aplicações gráficas
ENV DISPLAY=:0

# Executa o programa principal
CMD ["python", "main.py"]
