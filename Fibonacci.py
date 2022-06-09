def CalcularSerie(n):
    serie = [0, 1]
    if n == 0:
        return None
    if n == 1:
        return [0]
    if n == 2:
        return serie
    if n > 2:
        for i in range(2, n):
            serie.append(serie[i-1]+serie[i-2])
        return serie

