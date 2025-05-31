import json

from app import app, db
from models.heroes import Heroe

JSON_FILE = 'avengers_data.json' 

def insert_avengers_data():
    """
    Inserta los datos de los Vengadores desde un archivo JSON a la base de datos.
    """
    with app.app_context(): 
        try:
            
            db.create_all()
            print("Tablas de la base de datos verificadas/creadas.")

            
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            
            avengers = data.get('avengers', [])

            if not avengers:
                print(f"Advertencia: No se encontraron Vengadores en el archivo '{JSON_FILE}'. Asegúrate de que la clave principal sea 'avengers'.")
                return

            print(f"Encontrados {len(avengers)} Vengadores para insertar...")

            
            for avenger_data in avengers:
                
                habilidades_str = ", ".join(avenger_data.get('habilidades', []))

                
                heroe = Heroe(
                    nombre=avenger_data.get('nombre'),
                    alias=avenger_data.get('alias'),
                    habilidad=habilidades_str,
                    actor=avenger_data.get('actor')
                )
                db.session.add(heroe) 

            db.session.commit() 
            print("¡Datos de Vengadores insertados exitosamente!")

        except FileNotFoundError:
            print(f"Error crítico: El archivo '{JSON_FILE}' no se encontró en la ruta esperada. Asegúrate de que esté en la misma carpeta que 'insert_data.py'.")
        except json.JSONDecodeError:
            print(f"Error crítico: No se pudo decodificar el JSON del archivo '{JSON_FILE}'. Revisa su sintaxis para errores (comas, corchetes, comillas).")
        except Exception as e:
            db.session.rollback()
            print(f"Ocurrió un error inesperado al insertar los datos: {e}")
            print("Asegúrate de que tu base de datos esté corriendo y las credenciales en .env sean correctas.")

if __name__ == '__main__':
    print("Iniciando proceso de inserción de datos...")
    insert_avengers_data()
    print("Proceso de inserción de datos finalizado.")