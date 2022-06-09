import Fibonacci


def testFibonacciLetra(n='x'):
    serie = []
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci0(n=0):
    serie = []
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci1(n=1):
    serie = [0]
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci2(n=2):
    serie = [0, 1]
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci3(n=3):
    serie = [0, 1, 1]
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci4(n=4):
    serie = [0, 1, 1, 2]
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci5(n=5):
    serie = [0, 1, 1, 2, 3]
    assert Fibonacci.CalcularSerie(n) == serie


def testFibonacci6(n=6):
    serie = [0, 1, 1, 2, 3, 5]
    assert Fibonacci.CalcularSerie(n) == serie
