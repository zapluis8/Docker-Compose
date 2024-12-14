from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definimos el modelo base de SQLAlchemy
Base = declarative_base()

# URL de la base de datos SQLite
DATABASE_URL = "sqlite:///./characters.db"

# Configuración de la base de datos
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definimos el modelo 'Character' para la tabla 'characters'
class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    game = Column(String)
