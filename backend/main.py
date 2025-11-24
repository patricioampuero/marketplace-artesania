from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware  # <--- ESTO ES NUEVO
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from database import engine, SessionLocal
import models

# Crear tablas si no existen
try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Nota: {e}")

app = FastAPI()

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
# Esto permite que tu página web (localhost:5173) pida datos a este servidor
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitimos todo para facilitar el desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------------------------

# --- Esquemas ---
class ProductCreate(BaseModel):
    title: str
    description: str
    price: int
    category: str
    stock: int
    image_url: Optional[str] = None

class ProductResponse(ProductCreate):
    id: int
    class Config:
        from_attributes = True

# --- Conexión ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Rutas ---
@app.get("/")
def read_root():
    return {"status": "Backend Operativo 🚀"}

@app.get("/productos/", response_model=List[ProductResponse])
def leer_productos(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.post("/productos/", response_model=ProductResponse)
def crear_producto(producto: ProductCreate, db: Session = Depends(get_db)):
    nuevo_producto = models.Product(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto