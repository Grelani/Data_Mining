def elbow(data,min=2,max=8,max_iter=1000,tol=0.001,randomstate=None):
    inercias=[]
    for k in range(min,max+1):
        modelo=create_kmeans(data, n_clusters=k, max_iter=max_iter, tol=tol, randomstate=randomstate)
        kmeans_fit(modelo,verbose=False) #Para que no se vaya imprimir todo lo de cada iteracion
        inercias.append(inertia(modelo))
    x=list(range(min,max+1))
    y=inercias
    plt.plot(x, y, marker="o")
    plt.title("Método del codo")
    plt.xlabel("K")
    plt.ylabel("Inertia")
    plt.show()
    return None