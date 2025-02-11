""" EJERCICIO 2

Crea un cuento modelo que incluya al menos 10 datos diferentes personalizados d
el niño o niña al que va dirigido el cuento. La declaración de variables debe ser en bloque. 
Ejemplo:
ciudad, year, nombre_niño = "Bogotá", 2021, "Nicolás"
print("Amanece en " + ciudad + "en el año " + str(year)+ "..." ) """

ciudad, year, nombre_niño = "Campo Real", 2022, "Sergio"
color_pelo, altura_cm, peso_kg = "negro", 170, 63.0
color_ojos, genero, longitud_pelo, tamano_pie = "verdes", "chico", "corto", 40.5

print(f"En {str(ciudad)}, en el año {str(year)}, vivía un niño llamado {str(nombre_niño)}. "
      f"Con su pelo {str(color_pelo)} y ojos {str(color_ojos)}, {str(nombre_niño)} era un {str(genero)} de {str(altura_cm)} cm y {str(peso_kg)} kg. "
      f"Su pelo era {str(longitud_pelo)} y su talla de pie era {str(tamano_pie)}. "
      f"Una noche, vio a Papá Noel y, después de conversar, el mágico hombre de rojo le regaló unos guantes que podían cumplir cualquier deseo. "
      f"{str(nombre_niño)} decidió usar los guantes para compartir la alegría navideña con todos en {str(ciudad)}. ¡Feliz Navidad!")