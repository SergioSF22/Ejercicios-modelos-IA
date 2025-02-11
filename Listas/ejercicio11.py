""" EJERCICIO 11: Crea una nueva lista a partir de una lista que almacene valores numéricos del 1 al 30. 
La nueva lista solo almacenará los valores filtrados que se correspondan con números primos """
numeros = [i for i in range(1, 101)]
primos = [
    n
    for n in numeros
    if (n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0)
    or n == 1
    or n == 2
    or n == 3
    or n == 5
    or n == 7
]
print(primos)
