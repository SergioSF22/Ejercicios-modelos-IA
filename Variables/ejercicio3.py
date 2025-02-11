"""EJERCICIO 3: Crear un programa que le solicite al usuario sus datos para renovarse el DNI.
 Una vez que el usuario ha introducido los datos, el programa se los mostrará a modo de resumen
extra: formatear la entrada de datos utilizando el modulo regex"""

import re

validar_texto = r"\d+"
validar_sexo = r"^[HM]$"
validar_num = r"\D+"
validar_fecha = r"^(0[1-9]|[1-3][0-9])/(0[0-9]|1[0-2])/\d{4}$"

print("-------PROGRAMA DE RENOVACION DE DNI-------")

nombre = input("Introduce tu nombre y apellidos: ")
if re.search(validar_texto, nombre.upper()):
    nombre = "NO VALIDO"

edad = input("Introduce tu edad: ")
if re.search(validar_num, edad):
    edad = "NO VALIDO"

sexo = input("Introduce tu sexo (H/M): ").upper()
if not re.search(validar_sexo, sexo):
    sexo = "NO VALIDO"

nacionalidad = input("Introduce tu nacionalidad: ")
if re.search(validar_texto, nacionalidad.upper()):
    nacionalidad = "NO VALIDO"

fecha_nac = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
if not re.search(validar_fecha, fecha_nac):
    fecha_nac = "NO VALIDO"

print("--------RESUMEN DE TUS DATOS--------")
print(
    "Nombre: {}\nEdad: {}\nSexo: {}\nNacionalidad: {}\nFecha nacimiento: {}".format(
        nombre.title(), edad, sexo, nacionalidad.title(), fecha_nac
    )
)
