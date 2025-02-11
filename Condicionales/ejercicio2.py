"""Estás desarrollando un sistema que analiza la velocidad de los vehículos en una carretera. El sistema debe evaluar si un vehículo está cumpliendo con los límites de velocidad establecidos y categorizar su velocidad en función de su desempeño.

El sistema utilizará **operadores aritméticos**, **operadores de comparación** y un **condicional `if`** para determinar si el vehículo está dentro del límite de velocidad y si necesita una **advertencia** o una **multa**. También debe calcular un **descuento** en la multa si la velocidad es apenas superior al límite.

### **Instrucciones:**

1. **Recibe la velocidad del vehículo** como un número entero.
2. **Usa operadores aritméticos** para calcular el **exceso de velocidad** si la velocidad es mayor que el límite de velocidad de la carretera.
3. **Usa operadores de comparación** y un **condicional `if`** para determinar lo siguiente:
    - Si la velocidad es **igual o menor que el límite de velocidad** (120 km/h), no hay multa ni advertencia.
    - Si el exceso de velocidad es **menor o igual a 10 km/h**, se asigna una **advertencia** sin multa.
    - Si el exceso de velocidad es mayor a **10 km/h**, se asigna una **multa** de 120€.
    - Si la multa se aplica, se **aplica un descuento del 10%** si el exceso de velocidad no supera los **15 km/h**.
4. **Muestra** la velocidad del vehículo, el exceso de velocidad (si lo hay) y el mensaje correspondiente: **advertencia** o **multa**."""

# Definimos el limite de velocidad de la carreteta y la variable multa
speed_limit = 120
multa = 0

# Pedimos al usuario la velocidad del vehículo y validamos un dato
while True:
    speed = int(input("Introduce la velocidad del vehiculo: "))
    if speed < 0:
        print("DATO NO VÁLIDO")
    else:
        break

# Si la velocidad del usuario es mayor al límite calculamos el exceso de esta
if speed > speed_limit:
    speed_excess = speed - speed_limit
    # Evaluamos el exceso de velocidad si existe para ajustar el mensaje y la multa para el usuario
    if speed_excess <= 10:
        message = "Advertencia"
    elif speed_excess > 10:
        message = "Multa"
        multa = 120
        if speed_excess <= 15:
            multa -= multa * 0.1
else:
    speed_excess = 0
    message = "Todo bien"

# Mostramos los datos por pantalla al usuario
print("----------------DATOS--------------")
print(f"Velocidad del vehiculo: {speed} km/h")
print(f"Velocidad limite de la via: {speed_limit} km/h")
print(f"Exceso de velocidad: {speed_excess} km/h")
print(f"Mensaje: {message}")
print(f"Multa: {str(multa)}€")
print(".----------------------------------")
