import pandas as pd

def detect_outliers(data, method='iqr', 
threshold=1.5):
    if method=="iqr":
        return iqr(data,threshold)
    elif method=="zscore":
        return zscore(data,threshold)
    else:
        print("You've inserted a non valid strategy")

def zscore(df, threshold =1.5):
    df_copy = pd.DataFrame(False, index=df.index, columns=df.columns)
    columnas_numericas = df.select_dtypes(include=['int', 'float']).columns
    for columna in columnas_numericas:
        mean=df[columna].sum()/df[columna].count()
        std= df[columna].std(ddof=0)
        zscore=(df[columna]-mean)/std
        df_copy[columna]= zscore.abs()>threshold
    return df_copy

def iqr(df, threshold = 1):
    df_copy = pd.DataFrame(False, index=df.index, 
columns=df.columns)
    columnas_numericas =df.select_dtypes(include=['int', 'float']).columns
    for columna in columnas_numericas:
        q1=df[columna].quantile(0.25)
        q3=df[columna].quantile(0.75)
        iqr=q3-q1
        limite_sup=q3+threshold*iqr
        limite_inf=q1-threshold*iqr
        outliers=(df[columna]>limite_sup)|(df[columna]<limite_inf)
        df_copy[columna]=outliers
    return df_copy
