def CalcularSerie(n):
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1]+serie[i-2])
    return serie
