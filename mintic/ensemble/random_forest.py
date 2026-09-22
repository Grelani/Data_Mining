import numpy as np

def bootstrap_sample(X, y, random_state=None):
    X = np.asarray(X)
    y = np.asarray(y)
    rng = np.random.default_rng(random_state)
    tamaño=X.shape[0]
    nchoice = rng.choice(tamaño, size=tamaño, replace=True)
    return X[nchoice], y[nchoice]


def build_id3_tree(X, y):
    X = np.asarray(X)
    y = np.asarray(y)
    if y.ndim > 1:
        y = y.ravel()   #Aplana el array a una dim
    def entropy(y):
        clases,conteos=np.unique(y,return_counts=True)
        suma=np.sum(conteos)
        proporciones=conteos/suma
        entropia=np.sum(proporciones*np.log2(proporciones))*-1
        return entropia
    
    def information_gain(X, y, columnas):
        h_inicial = entropy(y)
        h_ponderada = 0
        for valor in np.unique(X[:, columnas]):
            mascara = X[:, columnas] == valor
            grupo = y[mascara]       
            peso = len(grupo)/len(y)
            h_ponderada += peso*entropy(grupo)
        return h_inicial-h_ponderada 

    def construir(X, y, columnas):
        if len(np.unique(y))==1:
            return y[0]
        if len(columnas)==0:
            clases, conteos=np.unique(y,return_counts=True)
            return clases[np.argmax(conteos)]
        ganancias=[]
        for c in columnas:
            ganancias.append(information_gain(X, y, c))
        mayor=columnas[np.argmax(ganancias)]
        nodo={mayor:{}}
        restantes = [c for c in columnas if c != mayor]
        for valor in np.unique(X[:, mayor]):
            mascara = X[:, mayor] == valor
            if mascara.any():
                nodo[mayor][valor] = construir(X[mascara], y[mascara], restantes)
            else:
                clases, conteos = np.unique(y, return_counts=True)
                nodo[mayor][valor] = clases[np.argmax(conteos)]
        return nodo
            
    return construir(X, y, list(range(X.shape[1])))



def build_random_forest(X,y, n_trees=10, random_state= None):
    X = np.asarray(X)
    y = np.asarray(y)
    lista_arboles=[]
    for n in range(n_trees):
        if random_state is not None:
            random_seed=random_state+n
        else:
            random_seed=None
        X_for,y_for=bootstrap_sample(X, y, random_state=random_seed)
        arbol=build_id3_tree(X_for,y_for)
        lista_arboles.append(arbol)
    return lista_arboles


def predict_ensemble(forest, X_test):
    X_test=np.asarray(X_test)
    
    def leaves(nodo):
            hojas=[]
            if type(nodo) == dict:
                for a in nodo.values():
                    hojas.extend(leaves(a))
            else:
                return [nodo]
            return hojas
        
    def predict_tree(tree, fila):
        if type(tree) == dict:
            columna=list(tree.keys())[0]
            valor=fila[columna]
            if valor not in tree[columna]:
                hojas=leaves(tree[columna])
                clases, conteos=np.unique(hojas, return_counts=True)
                return clases[np.argmax(conteos)]
            arbolito=tree[columna][valor]
            return predict_tree(arbolito, fila)
        else:
            return tree
    nueva=[]
    for fila in X_test:
        votos=[]
        for arbol in forest:
            prediction=predict_tree(arbol, fila)
            votos.append(prediction)
        clases, conteos = np.unique(votos, return_counts=True)
        moda=clases[np.argmax(conteos)] #Argmax ya da el más grande en orden alfabético en caso de empate
        nueva.append(moda)
        
    return np.array(nueva)
                
