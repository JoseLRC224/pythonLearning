import requests

def consultar_api():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    #url = "xdxd"
    print("--- Iniciando petición al servidor ---")
    
    try:
        # Intentamos hacer la petición
        respuesta = requests.get(url, timeout=5)
        
        # Esto lanza una excepción si el código de estado es de error (404, 500, etc.)
        respuesta.raise_for_status()
        
        # Si todo va bien, convertimos a diccionario
        datos = respuesta.json()
        print(f"Éxito. Título del post: {datos['title']}")
        
        # Guardamos el resultado en un archivo
        with open("log_api.txt", "a") as archivo:
            archivo.write(f"Post obtenido: {datos['title']}\n")
        print("💾 Resultado guardado en log_api.txt")

    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor. Revisa tu internet.")
    
    except requests.exceptions.HTTPError as err:
        print(f"❌ Error HTTP: {err}")
    
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")
    
    finally:
        print("--- Proceso finalizado ---")

if __name__ == "__main__":
    consultar_api()
