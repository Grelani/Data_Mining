import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def plot_missing(data):
    df_copy=data.copy()
    columnas=df_copy.columns
    valores_faltantes=df_copy.isnull().sum()
    plt.bar(columnas,valores_faltantes.values, color="lightcoral")   
    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title("Valores faltantes")
    plt.xlabel("Columnas")
    plt.ylabel("Número de valores faltantes")
    plt.show()