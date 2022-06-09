import Fibonacci


def testFibonacci(n=6):
    serie = [0, 1, 2, 3, 4, 5]
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci2(n=6):
    serie = [0, 1, 1, 2, 3, 5]
    assert Fibonacci.CalcularSerie(n) == serie
