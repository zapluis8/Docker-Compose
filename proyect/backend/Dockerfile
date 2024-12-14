# Usamos una imagen base de Python 3.9 que es ligera (slim)
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt desde el host al contenedor
COPY requirements.txt .

# Instalamos las dependencias que están en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de la carpeta 'app' del host al contenedor
COPY ./app ./app

# Comando para ejecutar la aplicación con Uvicorn, especificando que debe escuchar en todas las interfaces de red y en el puerto 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
