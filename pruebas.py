"""num = [1, 2, 3, 4, 5, 2, 1, 23, 4, 5]
min_valor = min(num)
max_valor = max(num)
normalizado = [(x - min_valor) / (max_valor - min_valor) for x in num]
normalizado.sort()
print(normalizado)"""

numeros = []
numeros.extend(range(1, 101))

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

lista = ["hola", "mundo", "python", "es", "genial"]
nueva_lista = [p for p in lista if "o" in p]
print(nueva_lista)
