def inertia(kmeans):
    puntos=kmeans["Puntos"]
    centroides=kmeans["Centroides"]
    etiquetas=kmeans["Etiquetas"]
    centroides_puntos=centroides[etiquetas]
    inercia=np.sum((centroides_puntos-puntos)**2)
    return inercia