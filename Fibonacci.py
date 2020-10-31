
'''


Sucesión de Fibonacci 

''''


# Importamos la librería sys para subir el limite de recursividad de Python.
import sys

# La función recursiva realiza varias veces los mismos cálculos.


def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# En cambio en la función dinámica vamos a utilizar la técnica de la
# memorización, guardando los resultados ya hechos en un diccionario.
def fibonacci_dinamico(n, memo={}):
    if n == 0 or n == 1:
        return 1

    # Primero intentamos buscar el resultado en memoria.
    try:
        return memo[n]

    # En caso de no existir realizamos el cálculo.
    except KeyError:
        resultado = fibonacci_dinamico(
            n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado


if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
