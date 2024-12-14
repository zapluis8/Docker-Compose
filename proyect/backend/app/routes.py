from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, Query
from app.models import SessionLocal, Character, Base

# Creamos la base de datos si no existe
Base.metadata.create_all(bind=SessionLocal().bind)

# Definimos el enrutador para las rutas de 'characters'
character_router = APIRouter(prefix="/characters")

# Función de dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para listar todos los personajes
@character_router.get("/")
def list_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()

# Ruta para crear un nuevo personaje
@character_router.post("/")
def create_character(name: str, game: str, db: Session = Depends(get_db)):
    character = Character(name=name, game=game)
    db.add(character)
    db.commit()
    db.refresh(character)
    return character

# Ruta para eliminar un personaje por ID
@character_router.delete("/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Caracter no encontrado")
    db.delete(character)
    db.commit()
    return {"detail": "Caracter eliminado correctamente"}

# Ruta para actualizar un personaje
@character_router.put("/{character_id}")
def update_character(character_id: int, name: str, game: str, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Caracter no encontrado")
    character.name = name
    character.game = game
    db.commit()
    db.refresh(character)
    return character
