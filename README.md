
# Proyecto de generación de personas

## Descripción
Este proyecto utiliza Python, SQLAlchemy, Faker y MySQL para
generar e insertar 100.000 registros de personas en una base
de datos local.

## Requisitos
- Python 3
- MySQL
- DBeaver
- Librerías indicadas en requirements.txt

## Instalación
Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
python -m pip install Faker
```

Configurar el archivo `.env` con la variable DATABASE_URL.

## Ejecución
Ejecutar el programa:

```bash
python main.py
```

## Tabla
El programa crea la tabla `personas_emanuel`, con una clave
primaria y atributos de información personal ficticia.

## Verificación
En DBeaver, ejecutar:

```sql
SELECT COUNT(*) FROM personas_emanuel;
```

El resultado esperado después de una ejecución exitosa es
100000.
