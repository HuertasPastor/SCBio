import openai
import os


# Código similar al anterior que tiene como objetivo recibir un archivo con código python y reenviarlo corregido
def corregir_codigo(ruta_archivo):
    # Cargamos el archivo de texto
    with open(ruta_archivo, "r") as archivo:
        codigo = archivo.read()

    # Creamos una instancia de la API de OpenAI
    openai.api_key = "API_KEY"
    modelo = "text-davinci-002"
    # Es necesario introducir tu propia clave API de open AI

    # Corregimos el código utilizando el modelo de OpenAI
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt="Fix the code: " + codigo,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Imprimimos la respuesta corregida en la consola
    ruta_correccion = os.path.splitext(ruta_archivo)[0] + "_fixed.py"
    with open(ruta_correccion, "w") as archivo_correccion:
        archivo_correccion.write(respuesta.choices[0].text)


# Ejemplo de uso
corregir_codigo("codigo.py")
