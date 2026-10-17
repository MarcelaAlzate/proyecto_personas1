
import os
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Date,
)
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "No se encontro DATABASE_URL en el archivo .env"
    )

engine = create_engine(DATABASE_URL)
Base = declarative_base()
fake = Faker("es_CO")

class Persona(Base):
    __tablename__ = "personas_emanuel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False)
    telefono = Column(String(30))
    ciudad = Column(String(100))
    direccion = Column(String(200))
    fecha_nacimiento = Column(Date)
    salario = Column(Float)

Session = sessionmaker(bind=engine)


def generar_personas(cantidad=100_000):
    personas = []

    for _ in range(cantidad):
        personas.append(
            Persona(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                correo=fake.unique.email(),
                telefono=fake.phone_number()[:30],
                ciudad=fake.city()[:100],
                direccion=fake.address()[:200],
                fecha_nacimiento=fake.date_of_birth(
                    minimum_age=18,
                    maximum_age=80,
                ),
                salario=round(
                    fake.pyfloat(
                        min_value=1300000,
                        max_value=8000000,
                        right_digits=2,
                    ),
                    2,
                ),
            )
        )

        if len(personas) >= 1000:
            yield personas
            personas = []

    if personas:
        yield personas


def main():
    Base.metadata.create_all(engine)

    session = Session()

    try:
        insertados = 0

        for grupo in generar_personas(100_000):
            session.add_all(grupo)
            session.commit()
            insertados += len(grupo)
            print(f"Personas insertadas: {insertados}")

        print("Proceso terminado correctamente.")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()
        engine.dispose()


if __name__ == "__main__":
    main()
