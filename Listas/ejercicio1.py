"""Tienes una lista de números enteros que representa la cantidad de ventas de un producto en diferentes días de la semana. Tu tarea es crear una nueva lista que contenga solo las cantidades de ventas que son **mayores o iguales a 50**, y simular un aumento en sus valores de un 10%.

**Requisitos:**

1. Utiliza **comprensión de lista** para filtrar las ventas que son mayores o iguales a 50.
2. Para cada valor que pase el filtro, **multiplica por 1.1**.
3. Al final, imprime la lista resultante."""

# Creamos la lista ventas con los enteros que representan las mismas
ventas = [65, 32, 78, 94, 21, 32, 43, 56, 78, 90]
# Utilizamos la compresion de listas para crear la lista con las ventas superiores o iguales a 50
ventasAltas = [i * 1.1 for i in ventas if i >= 50]
# Mostramos la nueva lista por pantalla
for i in ventasAltas:
    print(f"{i:.1f}")
