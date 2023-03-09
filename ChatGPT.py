import openai
import os


# Definimos la función que recibe la ruta del archivo txt
def generar_respuesta(ruta_archivo):
    # Cargamos el archivo de texto
    with open(ruta_archivo, "r") as archivo:
        texto = archivo.read()

    # Creamos una instancia de la API de OpenAI
    openai.api_key = "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"
    modelo = "text-davinci-002"

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
