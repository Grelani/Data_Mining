import pandas as pd

def input_missing(data, strategy= "mean", 
columns=None):
    if strategy=="mean":
        return mean(data, columns)
    elif strategy=="median":
        return median(data,columns)
    elif strategy == "mode":
        return mode(data,columns)
    else:
        print("You've inserted a non valid strategy")

def mean(df, columns=None):
    df_copy=df.copy()
    columnas_numericas = df.select_dtypes(include=['int', 'float']).columns
    if columns is not None:
        cols=[]
        for i in columnas_numericas:
            if i in columns:
                cols.append(i)
        columnas_numericas=cols
    
    for columna in columnas_numericas:
        mean= df_copy[columna].sum()/df_copy[columna].count()
        df_copy[columna]=df_copy[columna].fillna(mean)
    return df_copy

def median(df, columns=None):
    df_copy=df.copy()
    columnas_numericas = df.select_dtypes(include=['int', 'float']).columns
    if columns is not None:
        cols=[]
        for i in columnas_numericas:
            if i in columns:
                cols.append(i)
        columnas_numericas=cols
    for columna in columnas_numericas:
        median=df_copy[columna].sort_values().dropna()
        n=len(median)
        if n%2!=0:
            median=median.iloc[n//2]
        else:
            median=(median.iloc[n//2-1]+median.iloc[n//2])/2
        df_copy[columna]=df_copy[columna].fillna(median)
    return df_copy

def mode(df, columns=None):
    df_copy=df.copy()
    columnas=df_copy.columns
    if columns is not None:
        cols=[]
        for i in columnas:
            if i in columns:
                cols.append(i)
        columnas=cols
    for columna in columnas:
        repetidos={}
        for registro in df_copy[columna]:
            if registro in repetidos:
                repetidos[registro]+=1
            else:
                repetidos[registro]=1
        mode=max(repetidos, key=repetidos.get)
        df_copy[columna]=df_copy[columna].fillna(mode)
    return df_copy

