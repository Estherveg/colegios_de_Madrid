# Recopilador de información sobre colegios de Madrid capital.

import pandas as pd
import numpy as np
from funciones import centros_oficiales_CM,privados_concertados_fp_secundaria, busca_url_centro
from graficas import graf_1, EDA_tipos_centro

# Crear df de colegios de Madrid capital
df_colegios=centros_oficiales_CM()

print(df_colegios) #compruebo listado proporcionado por la CM
print(df_colegios.columns)

#EDA_tipos_centro(df_colegios)
df_filtrado=privados_concertados_fp_secundaria(df_colegios)
print("\nListado filtrado\n----------------")
print(df_filtrado) #compruebo listado filtrado
print(df_filtrado["DISTRITO MUNICIPAL"].value_counts())


# Busco en la web de la CM la lista filtrada de centros y añado sus url al df
df_priv_sec_url=busca_url_centro(df_filtrado)
# Guardo el df en un fichero csv
df_priv_sec_url.to_csv("centros_priv_secund.csv")
