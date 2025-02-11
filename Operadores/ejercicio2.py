"""Descripción: Imagina que estás trabajando en un algoritmo de clasificación para predecir si un paciente tiene o no una
enfermedad basándose en sus niveles de glucosa y presión arterial. Se te han proporcionado los datos de un paciente, y el
sistema predice si el paciente tiene o no la enfermedad (con una predicción de "1" si la predicción es positiva y "0" si es
negativa).

Tu tarea es evaluar el rendimiento del sistema de predicción, calculando el error absoluto y el error relativo, pero además,
debes comparar los valores reales con los predichos para determinar si el modelo ha subestimado o sobreestimado la condición
del paciente.

### Instrucciones:

1. Recibe las entradas de la glucosa real y la presión arterial real del paciente, junto con las predicciones del modelo
(en formato 1 o 0).
2. Calcula el error absoluto de cada característica (glucosa y presión arterial). El error absoluto es la diferencia entre el
valor real y el valor estimado, sin importar si es positiva o negativa (usa `abs()`).
3. Calcula el error relativo para ambas características (glucosa y presión arterial),
 usando la fórmula: `Error Relativo=(Error Absoluto / Valor Real)×100`
4. Calcula el rendimiento del modelo basado en las predicciones. Si las predicciones son correctas
(es decir, el modelo predijo correctamente el diagnóstico del paciente), asigna un punto al rendimiento.
 Si la predicción fue incorrecta, no se asignan puntos.
5. Calcula el puntaje final de rendimiento sumando los puntos por las predicciones correctas."""

# Pedimos los datos del paciente y la prediccion del modelo
glucosa_real = float(input("Introduce los niveles de glucosa (mg/dL): "))
presion_arterial_real = float(
    input("Introduce los niveles de presion arterial (mmHG): ")
)
prediccion_modelo = int(
    input("Introduce la prediccion del modelo para la glucosa (0 o 1): ")
)

# Definimos los niveles normales de glucosa y presion arterial
umbral_glucosa = 100
umbral_presion_arterial = 120

# Calculamos los errores absolutos de la glucosa y la presion arterial
error_abs_glucosa = abs(glucosa_real - umbral_glucosa)
error_abs_presion = abs(presion_arterial_real - umbral_presion_arterial)

# Calculamos los errores absolutos de la glucosa y la presion arterial
error_relativo_glucosa = (error_abs_glucosa / glucosa_real) * 100
error_relativo_presion = (error_abs_presion / presion_arterial_real) * 100

# Calculamos el rendimiento del modelo
puntuacion_modelo = 0
puntuacion_modelo += 1 * (
    ((glucosa_real != umbral_glucosa) and prediccion_modelo == 1)
    or (glucosa_real == umbral_glucosa and prediccion_modelo == 0)
)
puntuacion_modelo += 1 * (
    (presion_arterial_real != umbral_presion_arterial and prediccion_modelo == 1)
    or (presion_arterial_real == umbral_presion_arterial and prediccion_modelo == 0)
)

# Mostramos todas las variables por consola
print(f"Glucosa real: {glucosa_real} mg/dL")
print(f"Presion arterial real: {presion_arterial_real} mmHG")
print(f"Prediccion modelo enfermedad: {prediccion_modelo}")
print(f"Error absoluto glucosa: {error_abs_glucosa}")
print(f"Error absoluto presion arterial: {error_abs_presion}")
print(f"Error relativo glucosa: {error_relativo_glucosa:.2f}%")
print(f"Error relativo presion arterial: {error_relativo_presion:.2f}%")
print(f"Puntuacion del modelo: {puntuacion_modelo}")
