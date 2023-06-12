#Proyecto sobre webscraping para conseguir los últimos datos de la página de monoschinos, el objetivo es hacer una lista de los últimos animes en emisión, y poder descargar los vídeos y verlos con VLC

#Importar librerías
import requests
from bs4 import BeautifulSoup
import re
import sys
import os
import subprocess
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64


#Conseguir información: "Título", "Capítulo", "Enlace" y "Imagen" e imprimirlo

#Conseguir la página
url = "https://monoschinos2.com/"
page = requests.get(url)

#Comprobar que la página se ha conseguido
if page.status_code != 200:
    print("Error al conseguir la página")
    sys.exit()

#Crear el objeto BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

#Conseguir todos los divs con clase "col"
divs = soup.find_all("div", class_="col")

#Crear una lista vacía para guardar los datos
lista = []

#Recorrer todos los divs
for div in divs:
    
        #Conseguir el enlace del vídeo y el título del anime
        #Conseguir el enlace del vídeo
        enlace = div.find("a")["href"]
    
        #Conseguir el título del anime
        titulo = div.find("a")["title"]
    
        #Conseguir la dirección de la imagen
        imagen = div.find("img")["data-src"]
    
        #Conseguir el capítulo
        capitulo = div.find("p").text
    
        #Crear un diccionario con los datos
        diccionario = {
            "titulo": titulo,
            "capitulo": capitulo,
            "enlace": enlace,
            "imagen": imagen
        }
    
        #Añadir el diccionario a la lista
        lista.append(diccionario)

# Configurar el navegador
driver = webdriver.Firefox()

# Recorrer la lista
for diccionario in lista:
    print(diccionario["titulo"])

    # Conseguir el enlace de la página del vídeo
    enlace = diccionario["enlace"]

    # Conseguir la página del vídeo
    driver.get(enlace)

    # Esperar a que se cargue el div con id 'videoLoading'
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "videoLoading"))
        )
    except TimeoutError:
        print("Error al conseguir la página")
        driver.quit()
        sys.exit()

    # Conseguir el div con id 'videoLoading'
    div = driver.find_element(By.ID, "videoLoading")

    # Conseguir el enlace del reproductor del vídeo
    enlace = div.get_attribute("data-video")
    # El enlace está codificado en base64, así que hay que decodificarlo
    enlace = base64.b64decode(enlace).decode("utf-8")
    print(enlace)

    # Añadir el enlace del reproductor del vídeo al diccionario
    diccionario["enlace"] = enlace

# Cerrar el navegador
driver.quit()


#Guardar la lista en un archivo json
with open("./lista.json", "w") as archivo:
    json.dump(lista, archivo, indent=4)

# Llamar al script json-db.py que se encuentra en esta misma carpeta
subprocess.call(["python", "json-db.py"])