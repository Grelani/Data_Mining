def kmeans_fit(kmeans,verbose=True):
    puntos=kmeans["Puntos"]
    centroides=kmeans["Centroides"]
    max_iter=kmeans["Max_iter"]
    tol=kmeans["Tolerancia"]
    for i in range(max_iter):
        distancias=np.zeros((len(puntos), len(centroides)))
        for j,centroide in enumerate (centroides):
            distancias[:,j]=np.linalg.norm(puntos-centroide,axis=1)
        etiquetas=np.argmin(distancias, axis=1)
        nuevos_centroides=centroides.copy()
        for k in range (kmeans["N_clusters"]):
            mascara=etiquetas==k
            del_cluster=puntos[mascara]
            if len(del_cluster)>0:
                nuevos_centroides[k]=np.mean(del_cluster,axis=0)
            
        movimiento=np.linalg.norm(nuevos_centroides-centroides)
        if verbose:
            print(i, movimiento)
        centroides=nuevos_centroides
        if movimiento<tol: break

    kmeans["Centroides"]=nuevos_centroides
    kmeans["Etiquetas"]=etiquetas
    return kmeans

modelo=kmeans_fit(model)
print(modelo)