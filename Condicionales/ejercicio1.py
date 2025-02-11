"""Imagina que estás desarrollando un sistema de evaluación para un curso. Los estudiantes reciben una puntuación en el examen entre **0 y 100**, y tu tarea es calcular su rendimiento y determinar en qué categoría se encuentran, en función de la puntuación obtenida.

El sistema utilizará **operadores aritméticos**, **operadores de comparación** y un **condicional `if`** para determinar el **mensaje de rendimiento**. El sistema debe evaluar si el estudiante ha obtenido una puntuación suficiente para pasar el examen y categorizar el rendimiento con un mensaje específico.

### **Instrucciones:**

1. **Recibe la puntuación** del estudiante como un número entero entre **0 y 100**.
2. **Usa operadores aritméticos para calcular el puntaje ajustado del estudiante, se le aplica un descuento del 5% sobre la puntuación obtenida si la puntuación es inferior a 50. Y se añadirá un extra del 5% si la puntuación obtenida es mayor o igual a 60, o un 10% si la puntuación obtenida es mayor o igual a 80.
3. **Usa operadores de comparación** y un **condicional `if`** para determinar lo siguiente:
    - Si la puntuación ajustada es mayor o igual a **50**, el estudiante ha **aprobado** el examen.
    - Si la puntuación ajustada es **menor que 50**, el estudiante **no ha aprobado**.
    - Si el estudiante aprueba con una puntuación superior a **85**, se le dará un mensaje adicional de **excelente**.
    - Si el estudiante aprueba con una puntuación entre **50 y 85**, se le dará un mensaje de **aprobado**.
4. **Muestra** el puntaje ajustado y el mensaje correspondiente basado en la evaluación de la puntuación."""

# Pedimos al usuario la nota del estudiante con validacion de datos
while True:
    nota = int(input("Introduce la nota del alumno (entre 0 y 100): "))
    if nota > 100 or nota < 0:
        print("NOTA NO VÁLIDA")
    else:
        break

# Aplicamos la suma o la resta correpondiente a la nota
if nota >= 80:
    nota += nota * 0.1
elif nota >= 60:
    nota += nota * 0.05
elif nota < 50:
    nota -= nota * 0.05

# Asignamos un valor al mensaje que vamos a mostrar en funcion de la nota del estudiante
if nota >= 50:
    if nota > 100:
        mensaje = "Matricula"
    elif nota > 85:
        mensaje = "Excelente"
    else:
        mensaje = "Aprobado"
else:
    mensaje = "Suspenso"

# Imprimimos la nota y el mensaje por pantalla
print(f"NOTA: {str(nota)}")
print(f"MENSAJE: {mensaje}")
