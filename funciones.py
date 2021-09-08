
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


'''
Función para leer el fichero con listado de centros de la Comunidad de Madrid

Parámetros: no
Datos de entrada: url de la Comunidad de Madrid que aloja el listado
Return: fichero excel descargado en el escritorio

Funcionamiento: Busco el botón de descarga del fichero excel dentro la página web, lo pulso
y descargo el fichero en el escritorio
'''
# Abro un navegador Chrome y voy a la web de la CM
driver=webdriver.Chrome("/Users/estherveguillas/Desktop/Mi_curso/chromedriver")  #sin .exe
driver.implicitly_wait(40)
driver.get("https://gestiona3.madrid.org/wpad_pub/run/j/BusquedaAvanzada.icm") #web que quiero ver

#driver.find_element_by_id("btnDescargarListado").click()
driver.implicitly_wait(100)
print("hola")

driver.quit()


'''
Función para convertir en df el listado de centros de la CM


def centros_oficiales_CM():

    df_listado_centros = pd.read_csv("Data/centros_escolares_CMadrid.csv", sep=";", encoding='latin-1', header=[1])

    Para comprobar cómo se han importado los datos
    
    print(df_listado_centros.info())
    print(df_listado_centros.head(5))
    print(df_listado_centros.index)
    # Se observa que los nombres de las columnas se han desplazado 1 lugar a la derecha
    print("---------")

    # Corregir correlación nombre columna/dato
    nombres_columnas=list(df_listado_centros.columns) #lista con nombres originales
    #print("Nombres de las columnas:\n",nombres_columnas)

    new_nombres_columnas=list() #nueva lista con nombres desplazados.
    for index, columna in enumerate(nombres_columnas):
        if index<len(nombres_columnas)-1:
            new_columna=nombres_columnas[index+1]
            new_nombres_columnas.append(new_columna)
    dicc_columnas=dict(zip(nombres_columnas,new_nombres_columnas))
    #print("Nuevos nombres de las columnas:\n",new_nombres_columnas)
    df_listado_centros.drop(columns=["TITULARIDAD"],inplace=True) # Se elemina la última (no tiene datos)

    df_listado_centros.rename(columns=dicc_columnas,inplace=True) # Renombro las columnas con el nuevo listado
    #print(df_listado_centros["TITULARIDAD"]) #compruebo la nueva columna "TITULARIDAD" tiene los datos correctos
    # Index actual es columna con datos ("AREA TERRITORIAL"). Pongo como índice el código del centro
    df_listado_centros["AREA_TERRITORIAL"]=df_listado_centros.index
    df_listado_centros=df_listado_centros.set_index("CODIGO CENTRO")
    return df_listado_centros
'''