# Usamos la imagen base de Node.js versión 16
FROM node:16

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo package.json (y package-lock.json si existiera) al contenedor
COPY package.json ./

# Instalamos las dependencias definidas en package.json
RUN npm install

# Copiamos los archivos de la carpeta 'src' al contenedor en el directorio /app/src
COPY ./src ./src

# Copiamos los archivos estáticos de la carpeta 'public' al contenedor en el directorio /app/public
COPY ./public ./public

# Comando para iniciar la aplicación React
CMD ["npm", "start"]
