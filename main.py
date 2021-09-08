# Recopilador de información sobre colegios de Madrid capital.

import pandas as pd
import numpy as np
from funciones import centros_oficiales_CM
from graficas import graf_1, EDA_tipos_centro

# Crear df de colegios de Madrid capital
df_colegios=centros_oficiales_CM()

print(df_colegios) #compruebo listado proporcionado por la CM

EDA_tipos_centro(df_colegios)
