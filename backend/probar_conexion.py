import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# 1. Cargar datos del archivo .env
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

print("--- DIAGNÓSTICO DE DATOS ---")
print(f"Usuario detectado: {user}")
print(f"Servidor detectado: {host}")
print(f"Puerto detectado: {port}")
print("----------------------------")

# 2. Crear la URL de conexión de forma segura
database_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}?sslmode=require"

try:
    # 3. Intentar conectar
    engine = create_engine(database_url)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("\n✅ ¡ÉXITO TOTAL! CONEXIÓN ESTABLECIDA.")
        print(f"Versión de la base de datos: {result.fetchone()[0]}")
except Exception as e:
    print("\n❌ FALLÓ LA CONEXIÓN")
    print(f"El error es: {e}")