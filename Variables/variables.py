import keyword

# No requiere un ";" al final de cada línea
print("¡Hola mundo!")
print("¡Hola mundo!")
print("¡Hola mundo!")

# Comentarios en línea

""" Comentarios en bloque
Esto es un comentario en bloque
Y aquí lo finalizo """

# ESTRUCTURA BÁSICA DE UN SCRIPT EN PYTHON
""" 
1- Importación de módulos- Al inicio del archivo
2- Definición de funciones o variables -naming -> snake_case
3- Código principal """
# 1
import math  # noqa: E402


# 2
def calcular_area_circulo(radio):
    return math.pi * (radio**2)


radio = 8
# 3
print("El área del círculo es:", calcular_area_circulo(radio))

# CARACTERÍSTICAS DE SINTAXIS DE PYTHON

# **1**- Indentación: Python es un lenguaje que utiliza identación  para definir la estructura y los bloques de código
if True:
    print("Verdadero")

    # **2**- Tipado Dinámico: No necesitamos declarar el tipo de la variable explícitamente. El interprete de Python determina el tipo.
    """ - Naming de las variables
    - Tipos de datos básico
    - Tipos de datos complejos """
# 1. Naming variables
# a. Los nombre de variables no pueden comenzar con un número o con un caracter especial a especión del _
_numero = 5
numero = 6
# b. No debo sobrepasar los 79 caracteres, en caso de hacerlo debo utilizar el caracter \ para generar el break-salto de línea.
texto = "Some teams strongly prefer a longer line length. For code maintained \
    exclusively or primarily by a team that can reach agreement on this issue, it is okay to increase the line length limit up to 99 characters, provided that comments and docstrings are still wrapped at 72 characters."
# c. Por convención se utilizan minúsculas y snake_case para declarar variables cuyo naming incluya dos o más palabras. Los nombre de las variables siempre deben ser descriptivos
NOMBRE = "Alejandra"  # Esto no es correcto
nombre_y_apellido = "Alejandra Espinosa"  # snake_case
camelCase = "variable"  # Esto no es correcto
patatas_fritas = "Alejandra"  # Esto no es descriptivo ni correcto
# d. Puedo declarar variables en bloque
alias, anios, altura = "Ale", 78, 1.70
# e. No puedo utilizar palabras reservadas de la propia tecnologia
print(keyword.kwlist)

# 2. Tipos de datos
""" 
    - Las cadenas de caracteres pueden definirse con comillas dobles o simples indistantemente.
    - Los operadores siempre incluyen un espacio antes y después 
    """
dato_string = "cadena de caracteres 32323 %&//"
dato_string = "cadena de caracteres"
dato_numero_entero = 6
dato_numero_flotante = 6.5
dato_booleano = True
dato_booleano_2 = False


# a. Cadenas de caracteres - INDEX: El index (índice), hace referencia a la posición de cada uno de los caracteres dentro de una cadena. El primer index de toda cadena o colección de datos siempre va a ser el index 0
cadena = "Hola soy una cadena"
primer_caracter = cadena[0]
tercer_caracter = cadena[2]
print(cadena[0])  # Imprime la primera letra de la cadena
print(primer_caracter, tercer_caracter)
seccion_cadena = cadena[4:9]  # Incluye el primer index, pero excluye el último
print(seccion_cadena)
desde_caracter_a_final = cadena[
    9:
]  # Nos muestra los caracteres desde un index hasta el final.
desde_inicio_a_caracter = cadena[
    :8
]  # Nos muestra los caracteres desde el inicio hasta un index.
print(desde_caracter_a_final)
print(desde_inicio_a_caracter)
# cadena[5] = "g" --> No me permite reasignar valores de caracteres dentro de una cadena


""" TIPOS CONVERSIÓN DE DATOS 

¿Por qué es importante realizar conversiones de datos en Python?
    · Poder realizar operaciones coherentes.
    · Presentación de los datos
    · Interacción con los usuarios
    · Compatibilidad

TIPOS --->

1 - Casting de datos: Cambiar el tipo de dato de una variable
    numero_entero = int(3.14278974)
    numero_entero_dos = "El numero entero es" +  str(numero_entero)

2 - Concatenación de variables: Combinar variables de diferentes tipos en una cadena
    print("El nombre del usuario es " + name + " y su año de nacimiento es " + str(year))

3 - F-string: Simplificar la creacción de cadenas con variables. Surge con Python3
    name = "Carlos"
    age = 35
    mensaje = f"Hola mi nombre es {name} y mi edad es {age}"

4 - .format : Alternativa más antigua para formatear cadenas. Surgió con Python1
    El método format() se utiliza para construir cadenas que contienen valores de variables.
    La sintaxis básica es:    
    mensaje = "Hola {} y su edad es {}".format(name, age)  #{} -> Marcadores



"""

# nombre1 = str(input("Introduce tu nombre:\n"))
edad1 = 36
print("Tu edad es:" + str(edad1))
entero = 78
decimal = 6343
print(entero, decimal)
print(entero + decimal)
texto7 = "texto"
texto8 = "divisible"
print(texto7 + texto8)
print(texto7, texto8)

uno = int(3.14)
print(uno)

# f-string: su sintaxis comienza siempre por el caracter "f" antes de iniciar el string. Dentro del string podemos incluir las variables dentro de llaves
nombre = "Carlos"
edad = 35
mensaje = f"Hola mi nombre es {nombre} y mi edad es {edad}"
print(mensaje)
# Método .format
mensaje = "Hola {} y su edad es {}".format("Carlos", 35)
mensaje = "Hola mi nombre es", nombre, "y mi edad es", edad
mensaje = "Hola mi nombre es " + nombre + "y mi edad es " + str(edad)

# Entrada por teclado con la función input()
# tipodedato(input("texto de referencia para el usuario"))
nombre = input("Introduce tu nombre:\n").lower()
# edad = int(input("Introduce tu edad:\n"))
# peso_con_decimales = float(input("Introduce tu peso con decimales:\n"))
print(nombre)
# CONVERSIÓN A MAYÚSCULAS Y MINÚSCULAS
nombre = "Mariano"
# texto en minúsculas
print(nombre.lower())
# texto en mayúsculas
print(nombre.upper())
# texto en mayúsculas y minúsculas
print(nombre.title())
# textos en minúsculas y mayúsculas
print(nombre.swapcase())
