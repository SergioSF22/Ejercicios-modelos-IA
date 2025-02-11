"""- Ejercicio 10: Evaluación de los resultados de un torneo deportivo (for + if)

Estás encargado de analizar los resultados de un torneo deportivo donde los jugadores compiten en diferentes rondas. En cada ronda, los jugadores reciben una **puntuación** de 1 a 10, y tú necesitas calcular su **puntaje total** y su **promedio** de puntuaciones. Luego, debes determinar si su rendimiento ha sido **satisfactorio** en función de su puntaje total y su **promedio**.

Además, el sistema te pide que calcules el rendimiento de cada jugador en función de las puntuaciones recibidas, y realices un análisis de las puntuaciones más altas para cada jugador.

### **Instrucciones:**

1. **Recibe los datos de cada jugador**:
    - Nombre del jugador.
    - Puntuaciones de las diferentes rondas (una lista de puntuaciones entre 1 y 10).
    -

    ```python
    # Lista de jugadores con sus puntuaciones en cada ronda
    jugadores = [
        ["Juan", [8, 7, 6, 9]],
        ["Ana", [6, 7, 6, 6]],
        ["Luis", [9, 8, 10, 9]],
        ["Marta", [5, 6, 5, 6]]
    ]
    ```

2. **Calcula el puntaje total** de cada jugador, que es la **suma de todas las puntuaciones**.
3. **Calcula el promedio de puntuaciones** de cada jugador.
4. **Determina si el rendimiento del jugador fue satisfactorio**:
    - Si su puntaje total es mayor o igual a **30**, se considera satisfactorio.
    - Si su puntaje total es menor que **30**, no es satisfactorio.
5. **Usa comprensión de listas** para determinar:
    - Los jugadores con **puntajes satisfactorios**.
    - Los jugadores con **el puntaje más alto** en cada ronda.
6. **Muestra los resultados**:
    - El **puntaje total** de cada jugador.
    - El **promedio** de puntuaciones.
    - Si el rendimiento fue satisfactorio o no.
    - La lista de jugadores con **puntajes satisfactorios** y el **puntaje más alto** en cada ronda."""

# Definimos la lista jugadores con los datos de los mismos
players = [
    ["Juan", [8, 7, 6, 9]],
    ["Ana", [6, 7, 6, 6]],
    ["Luis", [9, 8, 10, 9]],
    ["Marta", [5, 6, 5, 6]],
]
# Recorremos la lista de jugadores
print("\n--------RESULTADOS TORNEO---------")
for i in players:
    print("----------------------------------")
    # Imprimimos por pantalla el nombre del jugador actual
    print(f"{i[0]}:")
    # Inicializamos a 0 la variable que llevara la puntuacion total de cada jugador al principio de cada iteracion
    total_score = 0
    # Recorremos la lista que contiene los puntajes por rondas del jugador actual y calculamos la puntuacion total
    for y in i[1]:
        total_score += y
    # En funcion de la puntuacion total y la longitud de la lista de los puntajes (numero de rondas realizadas), podemos calcular la puntuacion promedio del jugador
    average_score = total_score / len(i[1])
    print(f"    - Puntuacion total: {total_score}")
    print(f"    - Puntuacion promedio: {average_score:.2f}")
    # Evaluamos la puntuacion total del jugador actual para poder calificar su rendimiento y, en el caso de que se cumpla, añadir su registro a la lista de mejores jugadores con su nombre y puntaje mas alto
    if total_score >= 30:
        print("    - Rendimiento: Satisfactorio")
    else:
        print("    - Rendimiento: NO satisfactorio")
# Guardamos los registros de los jugadores con puntajes satisfactorios y su puntaje mas alto mediante la compresion de listas
best_players = [[i[0], max(i[1])] for i in players if sum(i[1]) >= 30]

# Recorremos la lista de mejores jugadores para imprimirlos por consola
print("\n--------MEJORES JUGADORES---------")
for i in best_players:
    print("----------------------------------")
    print(f"Nombre: {i[0]}")
    print(f"Mejor puntuacion: {i[1]}")
print("----------------------------------")
