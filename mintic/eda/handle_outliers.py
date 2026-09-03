def handle_outliers(data, method='iqr',action='trim', threshold=1.5):
    df_copy=data.copy()
    columnas_numericas = df_copy.select_dtypes(include=['int', 'float']).columns
    for columna in columnas_numericas:
        if method=="iqr":
            q1=df_copy[columna].quantile(0.25)
            q3=df_copy[columna].quantile(0.75)
            iqr=q3-q1
            limite_sup=q3+threshold*iqr
            limite_inf=q1-threshold*iqr
        elif method=="zscore":
            mean=df_copy[columna].sum()/df_copy[columna].count()
            std= df_copy[columna].std(ddof=0)
            limite_sup= mean+threshold*std
            limite_inf = mean-threshold*std
        else:
            print("You've inserted a non valid strategy")
            return data
            
        if action == "trim":
            df_copy=df_copy[(df_copy[columna] >= limite_inf) & (df_copy[columna]<= limite_sup)]
        elif action =="cap":
            df_copy[columna]=df_copy[columna].clip(lower=limite_inf, upper=limite_sup)
        else:
            print("You've inserted a non valid strategy")
        return data
    return df_copy