"""En un proyecto de programación de IA, se está trabajando con un conjunto de datos donde cada **muestra** está representada por un conjunto de características numéricas. El objetivo es clasificar cada muestra en dos categorías:

1. **Categoría 1**: Si la **suma** de las características es **menor o igual a 10**.
2. **Categoría 2**: Si la **suma** de las características es **mayor a 10**.

En este ejercicio, se te proporcionará una lista de **muestras** donde cada muestra es una lista con **valores numéricos**(características). Deberás clasificar cada muestra según su suma total y determinar en qué categoría cae.

### **Instrucciones:**

1. **Crea una lista de muestras**, donde cada muestra es una lista de características numéricas.
2. **Usa un bucle `for`** para recorrer cada muestra y calcular la **suma de sus características**.
3. **Clasifica la muestra** en una de las dos categorías:
    - **Categoría 1**: Si la suma de las características es menor o igual a 10.
    - **Categoría 2**: Si la suma de las características es mayor a 10.
4. **Almacena las categorías** de cada muestra en una nueva lista.
5. **Muestra la lista de categorías** de cada muestra."""

# Creamos la lista muestras con las listas que contiene las muestras numericas
# Inicializamos la lista vacia de categorias
muestras = [[5, 8, 1, 2], [1, 2, 3], [8, 2, 3], [0, 1, 0, 3, 4], [9, 8]]
categorias = []

# Bucle para iterar los elementos de la lista muestras
for x in muestras:
    # Igualo a 0 la variable suma cada vez recorro una lista nueva
    suma = 0
    # Recorro los elementos de la lista actual y los sumo todos en la variable suma
    for y in x:
        suma += y
    # Elijo la categoria de la lista en función de la suma total de sus elementos en la variable suma
    if suma <= 10:
        categorias.append("Categoria 1")
    else:
        categorias.append("Categoria 2")

# Bucle para iterar los elementos de la lista categorias y mostrarlos por pantalla
for i in categorias:
    print(i)
