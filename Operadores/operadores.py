"""# ******************** Operadores Aritméticos Básicos *******************
#Utilizamos operadores aritméticos para realizar cálculos y transformaciones sobre los datos.

# Suma
resultado_suma = 5 + 3  # 5 más 3 es igual a 8

# Resta
resultado_resta = 10 - 4  # 10 menos 4 es igual a 6

# Multiplicación
resultado_producto = 2 * 6  # 2 multiplicado por 6 es igual a 12

# División: Común en el cálculo de promedios, como al dividir la suma de errores entre el número de muestras.
resultado_division = 8 / 2  # 8 dividido por 2 es igual a 4.0 (resulta en un número de punto flotante)

# Cociente de la División: Para obtener resultados enteros, como el número de veces que un valor cabe en otro.
cociente_division = 8 // 2  # El cociente de dividir 8 entre 2 es 4 (resultado como número entero)

# Módulo (resto de la división): Útil para obtener el resto de la división, por ejemplo, en algoritmos de clasificación o agrupación.
resultado_modulo = 8 % 2  # El resto de dividir 8 entre 2 es 0

# Potencia: Común en IA para cálculos como el ajuste de pesos en redes neuronales.
resultado_potencia = 2 ** 3  # 2 elevado a la 3ra potencia es igual a 8

# Mostrar resultados
print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_producto}")
print(f"División: {resultado_division}")
print(f"Cociente de la División: {cociente_division}")
print(f"Módulo: {resultado_modulo}")
print(f"Potencia: {resultado_potencia}")"""

""" 
# ******************* Operadores de Asignación *******************

# Asignación simple
a = 5  # Se asigna el valor 5 a la variable 'a'

# Suma y Asignación (modificar el valor de una variable acumulada)
b = 3
b += a  # 'b' se incrementa por el valor de 'a'
b = b + a
# Resta y Asignación
c = 10
c -= 2  # 'c' se decrementa por 2
c = c - 2
# Multiplicación y Asignación
d = 4
d *= c  # 'd' se multiplica por el valor de 'c'
d = d * c
# División y Asignación
e = 8
e /= 2  # 'e' se divide por 2
e = e / 2
# Cociente de la División y Asignación
f = 9
f //= 3  # 'f' se divide por 3 y se asigna el cociente como número entero
f = f // 3
# Módulo y Asignación
g = 7
g %= 2  # 'g' se asigna con el resto de la división por 2
g = g % 2
# Potencia y Asignación
h = 2
h **= 3  # 'h' se eleva al cubo
h = h ** 3

# Mostrar resultados finales
print(f"Valor final de a: {a}")
print(f"Valor final de b: {b}")
print(f"Valor final de c: {c}")
print(f"Valor final de d: {d}")
print(f"Valor final de e: {e}")
print(f"Valor final de f: {f}")
print(f"Valor final de g: {g}")
print(f"Valor final de h: {h}")

# ******************* Operadores de Comparación *******************

# Igual a
a = 5
b = 5
resultado_igual = a == b  # 'True' si 'a' es igual a 'b', 'False' de lo contrario

# No igual a
c = 10
d = 7
resultado_no_igual = c != d  # 'True' si 'c' no es igual a 'd', 'False' de lo contrario

# Mayor que
e = 8
f = 4
resultado_mayor_que = e > f  # 'True' si 'e' es mayor que 'f', 'False' de lo contrario

# Menor que
g = 3
h = 6
resultado_menor_que = g < h  # 'True' si 'g' es menor que 'h', 'False' de lo contrario

# Mayor o igual que
i = 5
j = 5
resultado_mayor_igual = i >= j  # 'True' si 'i' es mayor o igual que 'j', 'False' de lo contrario

# Menor o igual que
k = 7
l = 9
resultado_menor_igual = k <= l  # 'True' si 'k' es menor o igual que 'l', 'False' de lo contrario

# Mostrar resultados finales
print(f"Resultado Igual a: {resultado_igual}")
print(f"Resultado No Igual a: {resultado_no_igual}")
print(f"Resultado Mayor que: {resultado_mayor_que}")
print(f"Resultado Menor que: {resultado_menor_que}")
print(f"Resultado Mayor o Igual que: {resultado_mayor_igual}")
print(f"Resultado Menor o Igual que: {resultado_menor_igual}")


# ******************* Operadores Lógicos *******************

# Operador AND (Y): Devuelve True si ambas condiciones son verdaderas, False de lo contrario.
a = True
b = True
resultado_and = a and b  

# Operador OR (O): Devuelve True si al menos una de las condiciones es verdadera, False de lo contrario.
c = True
d = False
resultado_or = c or d  

# Operador NOT (NO): Devuelve True si la condición es falsa, False de lo contrario.
e = True
resultado_not = not e  

# Mostrar resultados finales
print(f"Resultado AND (Y): {resultado_and}")
print(f"Resultado OR (O): {resultado_or}")
print(f"Resultado NOT (NO): {resultado_not}")



# ******************* OPERADORES DE IDENTIDAD *******************
# Verifican si dos variables apuntan a mismo objeto en memoria. En programación de IA, a veces necesitamos comprobar si dos variables apuntan al mismo objeto en la memoria, especialmente cuando estamos trabajando con referencias a objetos grandes (como modelos entrenados).  
#is: Devuelve True si ambas variables evaluadas apuntan al mismo objeto en la memoria
#is not: Devuelve True si ambas variables NO apuntan al mismo objeto en la memoria
#id(): Devuelve el identificador único de un objeto en la memoria

x = "Hola"
y = "Hola"
print(id(x), id(y)) # id indica la dirección del objeto en la memoria. El método id() nos devuelve la identidad de un objeto. 

# Diferencia entre operador is y operador ==
print(x == y)   # True, porque compara el valor
print(x is y)   # True, porque las dos variables apuntan al mismo objeto en memoria

x = 10
y = x
print(id(x), id(y))

#Operador is
a = 10
b = 10
print(a is b)   #True, porque ambos son referencias a el valor numerico 10 y Python optimiza el espacio alojándolas en el mismo espacio de memoria

#Operador is not
x = 10
y = 11
print("resultado de is not", x is not y) #True, porque las dos valiables apuntan a diferentes objetos en la memoria


# ******************* OPERADORES DE PERTENENCIA / MEMBRESIA *****************

#Nos permiten saber si un elemento esta contenido en una secuencia.
#- Operador in: Nos devolverá True si el elemento se encuentra en la secuencia, nos devolverá False si el elemento no se encuentra en la secuencia
#- Operador not in:  Nos devolverá True si el elemento no se encuentra en la secuencia, nos devolverá False si el elemento se encuentra en la secuencia

fruta = "manzana"

# Verificando si 'a' está en la palabra 'manzana'
resultado_in = "a" in fruta  # True, porque 'a' está en "manzana"

# Verificando si 'z' no está en la palabra 'manzana'
resultado_not_in = "z" not in fruta  # False, porque 'z' está en "manzana"



# EJEMPLO 1 --> Calcular el error absoluto y el error relativo de las ventas

# Datos de ventas
real_ventas = int(input("Introduce las ventas reales:\n"))
predicho_ventas = int(input("Introduce las ventas estimadas:\n"))

# Calcular el error absoluto
error_absoluto = abs(predicho_ventas - real_ventas)  # Usamos abs() para obtener el valor absoluto (no nos importa si diferencia es positiva o negativa)
#El error absoluto es simplemente la diferencia entre el valor real y el valor predicho, sin importar si es positiva o negativa.

# Calcular el error relativo (porcentaje de error)
error_relativo = (error_absoluto / real_ventas) * 100  # El error relativo como porcentaje
#El error relativo se calcula con la fórmula: (error absoluto / valor real) * 100

# Operación para determinar si se ha ganado o perdido
resultado = predicho_ventas < real_ventas  # Si predicho_ventas es menor que real_ventas, resultado será True (perdimos)
# Esto nos dirá con un valor booleano si hemos tenido más ventas de las estimadas o menos

# Mostrar los resultados
print(f"Error Absoluto: {error_absoluto}")
print(f"Error Relativo: {error_relativo:.2f}%")  # Mostrar el porcentaje con dos decimales, los : se usan dentro del f-string para formatear una salida
print(f"¿Se ha ganado más de lo estimado? {resultado}")  # Si no hemos perdido, significa que hemos ganado más
 """

# EJEMPLO 2 --> Evaluar rendimiento
# Datos del estudiante
horas_estudio = int(input("Introduce las horas de estudio:\n"))
ejercicios_resueltos = int(input("Introduce el número de ejercicios resueltos:\n"))

# Umbrales definidos para el rendimiento
umbral_horas = 8  # Umbral de horas de estudio (mínimo recomendado)
umbral_ejercicios = 20  # Umbral de ejercicios resueltos (mínimo recomendado)

# Evaluación del rendimiento utilizando operadores de comparación
# Verificamos si el estudiante ha cumplido con los umbrales
rendimiento_horas = (
    horas_estudio >= umbral_horas
)  # True si las horas de estudio son mayores o iguales al umbral
rendimiento_ejercicios = (
    ejercicios_resueltos >= umbral_ejercicios
)  # True si los ejercicios resueltos son mayores o iguales al umbral

# Usamos operadores de asignación para ajustar el rendimiento basado en las evaluaciones
rendimiento_final = 0  # Inicializamos el rendimiento final

# Asignamos puntos al rendimiento final usando operadores aritméticos de asignación
rendimiento_final += 5 * rendimiento_horas  # Si cumple el umbral de horas, suma 5
rendimiento_final += (
    5 * rendimiento_ejercicios
)  # Si cumple el umbral de ejercicios, suma 5

# Mostrar los resultados
print(f"Rendimiento de horas de estudio cumplido: {rendimiento_horas}")
print(f"Rendimiento de ejercicios resueltos cumplido: {rendimiento_ejercicios}")
print(f"Rendimiento final: {rendimiento_final}")
