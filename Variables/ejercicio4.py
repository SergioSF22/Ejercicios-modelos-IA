"""EJERCICIO 4: Crea un programa que simule un gestor de información de un diario.
 Para ello el programa deberá solicitar al usuario que introduzca la fecha con formato DÍA DE LA SEMAMA +
   día del mes (en número) + mes. Además en una nueva instrucción le pedirá al usuario que introduzca la hora
     y en una nueva instrucción le pedirá el texto de la entrada que desea almacenar. Al finalizar el programa
     mostrará al usuario toda la información con el siguiente formato:

• fecha string en mayúscula

• hora string

• texto de la entrada del diario en minúscula.

Extra: utiliza el módulo  date para almacenar la fecha de las entradas"""

from datetime import date
import datetime

validar_hora = r"^([0-1][0-9]|2[0-4]):([0-5][0-9])$"
validar_fecha = r"^(\D+)/(0[1-9]|[1-3][0-9])/(\D+)$"

print("-------DIARIO--------")
date_string = input(
    "Introduce la fecha con formato DÍA DE LA SEMAMA / día del mes (en número) / mes: "
)
date_data = date_string.split("/")
match date_data[2].upper():
    case "ENERO":
        mes = 1
    case "FEBRERO":
        mes = 2
    case "MARZO":
        mes = 3
    case "ABRIL":
        mes = 4
    case "MAYO":
        mes = 5
    case "JUNIO":
        mes = 6
    case "JULIO":
        mes = 7
    case "AGOSTO":
        mes = 8
    case "SEPTIEMBRE":
        mes = 9
    case "OCTUBRE":
        mes = 10
    case "NOVIEMBRE":
        mes = 11
    case "DICIEMBRE":
        mes = 12
year = datetime.date.today().year
fecha = date(year, mes, int(date_data[1]))

hora = input("Introduce la hora actual (hh:mm): ")
texto = input("Introduce el texto de la entrada de tu diario: ")
date_print = (
    date_data[0].title()
    + " "
    + str(fecha.day)
    + " de "
    + date_data[2].title()
    + " de "
    + str(fecha.year)
)
print(
    "FECHA: {}\nHORA: {}\nCONTENIDO: {}".format(date_print.upper(), hora, texto.lower())
)
