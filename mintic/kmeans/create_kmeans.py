def create_kmeans(data, n_clusters=8, max_iter=1000, tol=0.0001,randomstate=None):
    rng=np.random.default_rng(randomstate) #Es pars generar el punto aleatorio}
    puntos=data.to_numpy()  #Convertimos a numoy para que sea más fácil
    indices=rng.choice(len(data), size=n_clusters, replace=False) #Tomaremos un punto random de la bd, para que no salga de los rangos en donde se encuentra los datos
    centroides=puntos[indices].copy()   #Asignamos los centroides
    diccionario={"Puntos": puntos,"Centroide":centroides, "N_clusers":n_clusters, "Max_iter":max_iter, "Tolerancia": tol, "Rng": rng, "Etiquetas": None} #Guardamos en el diccionario
    return diccionario

