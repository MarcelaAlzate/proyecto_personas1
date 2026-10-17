
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

url = os.getenv("DATABASE_URL")

if not url:
    raise ValueError("No se encontro DATABASE_URL en el archivo .env")

engine = create_engine(url)

try:
    with engine.connect() as conexion:
        version = conexion.execute(
            text("SELECT VERSION()")
        ).scalar_one()

        print("Conexion exitosa con MySQL")
        print("Version de MySQL:", version)

except Exception as error:
    print("No se pudo conectar a MySQL.")
    print("Detalle del error:", error)

finally:
    engine.dispose()


