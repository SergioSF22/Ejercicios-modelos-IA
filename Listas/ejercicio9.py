""" Estás trabajando en un sistema que evalúa el rendimiento de ventas de productos de diferentes categorías durante el mes. Cada producto tiene un **precio** y el número de **unidades vendidas**. El sistema también **predice el número de unidades vendidas** basado en análisis de datos previos.

Tu tarea consiste en:

1. **Evaluar el error de la predicción** de ventas en cuanto a unidades y calcular el **error absoluto** y el **error relativo**.
2. **Actualizar los ingresos** proyectados multiplicando las ventas reales por un incremento de un **10%** para aquellas categorías de productos con ventas reales superiores a **50 unidades**.
3. **Filtrar productos** en base a sus ventas y el rendimiento de las predicciones usando listas.

### **Instrucciones:**

1. **Recibe los datos de ventas** y predicciones para cada producto:
    - Número de **unidades vendidas** reales.
    - Número de **unidades predichas**.
    - El **precio** de cada producto.

    # Lista de productos [unidades vendidas reales, unidades predichas, precio]
    productos = [
        [60, 50, 20],  # Error absoluto = 10
        [40, 45, 15],  # Error absoluto = 5
        [70, 65, 30],  # Error absoluto = 5
        [30, 25, 25],  # Error absoluto = 5
        [90, 80, 50]   # Error absoluto = 10
    ]
    
2. **Calcula el error absoluto** y el **error relativo** para las unidades vendidas comparando las ventas reales con las predicciones. El **error relativo** debe expresarse como un porcentaje.
3. **Filtra los productos** que tengan ventas **reales mayores o iguales a 50** unidades y multiplica sus ingresos (ventas reales * precio) por un **10% adicional**.
4. **Usa comprensión de listas** para crear listas de productos que cumplan con ciertos criterios (ventas reales mayores que 50 y predicción correcta).
5. **Muestra el resultado** con el cálculo del **ingreso ajustado** y el **puntaje final** de predicción (si la predicción fue correcta). """

# Lista de productos [unidades vendidas reales, unidades predichas, precio]
productos = [
    [60, 60, 20],
    [40, 45, 15],
    [70, 65, 30],
    [30, 25, 25],
    [90, 80, 50],
]
# Creamos la lista mediante compresion indicada en el paso 4
productos_compresion = [i for i in productos if i[0] > 50 and (i[0] == i[1])]
# Inicializamos un contador para saber por que iteracion de venta vamos
contador = 0
# Recorremos los datos de las ventas
for i in productos:
    # Sumamos 1 a nuestro contador
    contador += 1
    # Calculamos el error abs y rel de la venta de la iteracion actual y los mostramos por pantalla
    error_abs = abs(i[0] - i[1])
    error_rel = (error_abs / i[0]) * 100
    print("-------------------------------------")
    print(f"Venta {contador}:")
    print(f"    - Error absoluto: {error_abs}")
    print(f"    - Error relativo: {error_rel:.2f}%")
    # Evaluamos el rendimiento del modelo y damos un puntaje a su prediccion sobre la iteracion actual (True si ha acertado y False si no). Imprimimos el resultado por pantalla
    if error_abs == 0:
        puntaje = True
    else:
        puntaje = False
    print(f"    - ¿Ha acertado el modelo?: {puntaje}")
    # Evaluamos si la venta de la iteracion actual supera las 50 unidades reales vendidas, de ser asi calculamos su ingreso ajustado y lo mostramos por pantalla
    if i[0] >= 50:
        ingreso_ajustado = (i[0] * i[2]) * 1.1
        print(f"    - Ingreso ajustado: {ingreso_ajustado}")
print("-------------------------------------")
