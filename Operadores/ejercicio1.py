""" Estás trabajando en un **sistema de recomendación** que predice la calificación que un usuario le dará a una película. 
El sistema genera una **predicción** de la calificación, pero deseas **evaluar su precisión** comparando las calificaciones 
reales dadas por el usuario con las predicciones.

Tu tarea es calcular el **error absoluto** y el **error relativo** entre las calificaciones reales y las predicciones. 
Además, debes determinar si la **predicción fue superior o inferior** a la calificación real.

### **Instrucciones:**

1. Recibe los datos de la calificación real (de 1 a 5) y la predicción del sistema (de 1 a 5) como entradas desde el usuario.
2. Calcula el error absoluto entre la calificación real y la predicción. El error absoluto es la diferencia entre ambos valores,
 sin importar si es positiva o negativa (utiliza `abs()`).
3. Calcula el error relativo como un porcentaje, usando la fórmula: `Error Relativo =(ErrorAbsoluto / CalificacionReal )×100`
4. Determina si la predicción fue superior o inferior a la calificación real. Si la predicción es mayor, el sistema sobreestimó la 
calificación. Si la predicción es menor, el sistema subestimó la calificación. Almacena el resultado como un valor booleano y 
muestra el mensaje correspondiente.
5. Usa operadores de asignación para ajustar un puntaje de confianza en el sistema. Si la predicción es exacta (sin error absoluto),
 añade 10 puntos al puntaje de confianza. Si el error absoluto es menor o igual a 1, añade 5 puntos. Si el error absoluto es mayor
   que 1, no añades puntos. """

#Pedimos las variables al usuario
real_calification = int(input("Introduce la calificacion de la pelicula (1 a 5): "))
system_prediction = int(input("Introduce la prediccion del sistema (1 a 5): "))

#Calculamos el error absoluto
absolute_error = abs(real_calification - system_prediction)

#Calculamos el error relativo
relative_error = (absolute_error / real_calification) * 100

#True si el sistema sobreestimo la calificacion o False si la subestimo
prediction_value = system_prediction > real_calification

#Inicializamos la puntuacion en 0 y le sumamos 5 o 10 en funcion de que condicion se cumpla
confidence_score = 0
confidence_score += 5 * (absolute_error <= 1 and absolute_error > 0)
confidence_score += 10 * (absolute_error == 0)

#Mostramos todas las variables por consola
print(f"Calificación real: {real_calification}")
print(f"Predicción del sistema: {system_prediction}")
print(f"Error absoluto: {absolute_error}")
print(f"Error relativo: {relative_error:.2f}%")
print(f"Valor de la prediccion: {prediction_value}")
print(f"Puntaje de confianza: {confidence_score}")
