from fastapi import FastAPI
from app.routes import character_router

# Creamos una instancia de FastAPI, que es la aplicación principal
app = FastAPI(title="Videojuegos API", version="0.1")

# Incluimos las rutas definidas en el archivo routes.py
app.include_router(character_router)
