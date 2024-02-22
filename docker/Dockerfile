# imagem Python como base
FROM python:3

# Define o diretório de trabalho dentro do contêiner
WORKDIR /opt/simple-http-server

# Depedências
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

# Copia o script e o arquivo HTML para o contêiner

COPY index.html .

COPY httpd.py .

# Expõe a porta em que o aplicativo será executado
EXPOSE 3002

# Comando para executar o app quando o contêiner for iniciado
CMD ["python", "httpd.py"]
