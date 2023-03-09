import openai
import os


# Definimos la función que recibe la ruta del archivo txt
def generar_respuesta(ruta_archivo):
    # Cargamos el archivo de texto
    with open(ruta_archivo, "r") as archivo:
        texto = archivo.read()

    # Creamos una instancia de la API de OpenAI
    openai.api_key = "API_KEY"
    modelo = "text-davinci-002"
    # Es necesario introducir tu propia clave API de open AI

    # Generamos la respuesta utilizando el modelo de OpenAI
    respuesta = openai.Completion.create(
        engine=modelo,  # El modelo determina el formato de la respuesta de OpenAI
        prompt=texto,  # El texto es lo que le enviamos
        max_tokens=1024,  # Tokens determina la longitud máxima posible de la respuesta
        n=1,  # Numero de respuestas que queremos generar
        stop=None,  # Condición final de la repsuesta
        temperature=0.7,  # Factor de aleatoriedad de la repsuesta, cuanto más alto sea más creativa será esta
    )

    # Escribimos la respuesta en un archivo de texto
    ruta_respuesta = os.path.splitext(ruta_archivo)[0] + "_response.txt"
    with open(ruta_respuesta, "w") as archivo_respuesta:
        archivo_respuesta.write(respuesta.choices[0].text)


# Ejemplo de uso
generar_respuesta("texto.txt")
