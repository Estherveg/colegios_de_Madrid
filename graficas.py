import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def graf_1(df):

    plt.figure(figsize=(17,5))
    sns.countplot(df["TIPO DE CENTRO"])
    return

def EDA_tipos_centro(df):
    print("Tipos de centros")
    print("----------------")
    print(df["TIPO DE CENTRO"].value_counts())

    print("\nTitularidad")
    print("-----------")
    print(df["TITULARIDAD"].value_counts())
    return

