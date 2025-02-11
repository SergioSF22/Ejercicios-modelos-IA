"""Estás desarrollando un sistema de clasificación de temperaturas para una aplicación meteorológica. El sistema recibe una lista de temperaturas diarias en grados Celsius y clasifica cada día como **"Frío"**, **"Templado"** o **"Caluroso"** según el valor de la temperatura.

- Si la temperatura es menor a **10°C**, el día es **"Frío"**.
- Si la temperatura está entre **10°C y 25°C** (inclusive), el día es **"Templado"**.
- Si la temperatura es mayor a **25°C**, el día es **"Caluroso"**.

El sistema debe mostrar una lista con las clasificaciones correspondientes de cada día (Frío, Templado, o Caluroso).

### **Instrucciones:**

1. **Crea una lista de temperaturas diarias** (en grados Celsius).
2. **Usa un bucle `for`** para recorrer la lista de temperaturas y clasificar cada temperatura como "Frío", "Templado" o "Caluroso" según las condiciones mencionadas.
3. **Almacena las clasificaciones** en una nueva lista.
4. **Muestra la lista de clasificaciones** de temperaturas."""

# Creamos la lista grados con las temperaturas diarias en Celsius y la lista vacia que almacenara los estados de dichas temperaturas
grados = [32, 12, 20, 1, 40]
temperaturas = []

# Recorremos la lista grados y vamos evaluando sus valores para asignar el valor correspondiente a la lista de temperaturas
for i in grados:
    if i > 25:
        temperaturas.append("Caluroso")
    elif i >= 10 and i <= 25:
        temperaturas.append("Templado")
    else:
        temperaturas.append("Frio")

# Recorremos la lista temperaturas para imprimir sus valores por pantalla
for i in temperaturas:
    print(i)
