"""Estás desarrollando un modelo de **inteligencia artificial** que predice si un estudiante aprobará o no un examen, en función de varias características como el **tiempo de estudio** y el **número de ejercicios realizados**. Tienes una lista de datos sobre varios estudiantes, donde cada estudiante tiene dos características: el **tiempo de estudio** (en horas) y el **número de ejercicios realizados**.

Tu tarea es **filtrar aquellos estudiantes** que:

1. **Hayan estudiado más de 5 horas**.
2. **Hayan hecho más de 10 ejercicios**.

Cada estudiante está representado por una **lista** con dos elementos: el primer elemento es el **tiempo de estudio** y el segundo es el **número de ejercicios realizados**.

**Requisitos:**

1. Utiliza **comprensión de lista** para seleccionar solo los estudiantes que cumplen con las condiciones mencionadas.
2. Los estudiantes deben tener **más de 5 horas de estudio** y **más de 10 ejercicios realizados**.
3. La salida debe ser una lista de **listas** con los estudiantes que cumplen estas condiciones."""

# Creamos la lista estudiantes con listas que representan sus horas y ejercicios respectivamente
estudiantes = [[6, 12], [4, 15], [7, 23], [12, 34], [1, 1], [0, 0], [5, 10], [10, 5]]
# Mediante la compresion de listas creamos la cual almacenara los estudiantes que cumplan las condiciones
aprobados = [i for i in estudiantes if i[0] > 5 and i[1] > 10]
# Imprimimos la nueva lista por pantalla
for i in aprobados:
    print(i)
