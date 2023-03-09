
# Definimos la función que recibe la ruta del archivo txt
import openai
import os


def generar_respuesta(ruta_archivo):
    # Cargamos el archivo de texto
    with open(ruta_archivo, "r") as archivo:
        texto = archivo.read()

    # Creamos una instancia de la API de OpenAI
    openai.api_key = "API_AI_KEY"
    modelo = "text-davinci-002"
    # Es necesario introducir tu propia clave API de open AI

    # Generamos la respuesta utilizando el modelo de OpenAI
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=texto,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Escribimos la respuesta en un archivo de texto
    ruta_respuesta = os.path.splitext(ruta_archivo)[0] + "_response.txt"
    with open(ruta_respuesta, "w") as archivo_respuesta:
        archivo_respuesta.write(respuesta.choices[0].text)


# Ejemplo de uso
generar_respuesta("texto.txt")