# Use uma imagem base do Python
FROM python:3.13.3

# Define o diretório de trabalho
WORKDIR /app

# Copia os requisitos primeiro para aproveitar o cache de camadas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto da aplicação
COPY . .

# Expõe a porta do Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD python ./app.py
