import json
from app import app, db 
from models.heroes import Heroe 

JSON_FILE = 'avengers_data.json'

def insert_avengers_data():
    with app.app_context(): 
        try:
            
            db.create_all()
            print("Tablas de la base de datos verificadas/creadas.")

            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            avengers = data.get('avengers', [])

            if not avengers:
                print("No se encontraron Vengadores en el archivo JSON. Asegúrate de que la clave principal sea 'avengers'.")
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
            print(f"Error: El archivo '{JSON_FILE}' no se encontró. Asegúrate de que esté en la misma carpeta que insert_data.py.")
        except json.JSONDecodeError:
            print(f"Error: No se pudo decodificar el JSON del archivo '{JSON_FILE}'. Revisa su sintaxis.")
        except Exception as e:
            db.session.rollback() 
            print(f"Ocurrió un error al insertar los datos: {e}")

if __name__ == '__main__':
    insert_avengers_data()