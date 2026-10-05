def euclidean_distance(point1, point2):
    suma=0
    if len(point1)==len(point2):
        for punto in range(len(point1)):
            suma+=(point1[punto]-point2[punto])**2
        return suma**0.5
    else:
        return "Error, las listas no son de la misma longitud"
