# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
# #Crear una lista con múltiplos de 4 del 1 al 100
# multiplos_de_cuatro = list(range(4, 101, 4))
# print(multiplos_de_cuatro)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
# favoritos = ["los gatos", "las peliculas", "la música", "el café", "la programación"]

# # Accediendo al penúltimo elemento utilizando indexación negativa
# penultimo_elemento = favoritos[-2]
# print(f"El penúltimo elemento de la lista es: {penultimo_elemento}")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo:
# # Crear una lista vacía
# lista_vacia = []
# # Agregar tres palabras con append
# lista_vacia.append('café')
# lista_vacia.append('té')
# lista_vacia.append('mate')

# # Imprimir la lista resultante
# print("Lista resultante:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
# # Lista original
# animales = ["perro", "gato", "conejo", "pez"]
# # Reemplazando el segundo elemento (índice 1) con "loro"
# animales[1] = "loro"

# # Reemplazando el último elemento (índice -1) con "oso"
# animales[-1] = "oso"

# print(f"La lista de animales modificada es: {animales}")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print()

# 1. Se crea una lista llamada numeros que contiene cinco números enteros: 8, 15, 3, 22, 7.
# 2. Se usa max(numeros) para encontrar el número más grande en esa lista, que es 22.
# 3. Se usa remove(...) para eliminar ese número (22) de la lista.
# 4. La función print() se llama sin ningún argumento dentro de los paréntesis. Cuando se usa de esta manera, simplemente imprime una línea en blanco en la consola.


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
# # Crear la lista con números del 10 al 30, saltando de 5 en 5
# lista_saltos_de_cinco = list(range(10, 31, 5))
# print(f"La lista completa es: {lista_saltos_de_cinco}")

# # Mostrando los dos primeros elementos utilizando slicing
# dos_primeros = lista_saltos_de_cinco[0:2]
# print(f"Los dos primeros elementos de la lista son: {dos_primeros}")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
# # Lista original
# autos = ["sedan", "polo", "suran", "gol"]

# # Reemplazando los valores en los índices 1 y 2
# autos[1:3] = ["tracker", "kangoo"]

# print(f"La lista de autos modificada es: {autos}")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
# # Crear una lista vacía
# dobles = []

# # Agregar el doble de 5, 10 y 15
# dobles.append(5 * 2)
# dobles.append(10 * 2)
# dobles.append(15 * 2)

# # Imprimir la lista resultante
# print(f"La lista de los dobles es: {dobles}")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# # Lista original de compras
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# # a) Agregar "jugo" a la lista del tercer cliente usando append.
# compras[2].append("jugo")

# # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# compras[1][1] = "tallarines"

# # c) Eliminar "pan" de la lista del primer cliente.
# compras[0].remove("pan")

# # d) Imprimir la lista resultante por pantalla
# print(f"La lista de compras resultante es: {compras}")


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False

# # Crear la lista anidada
# lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# # Imprimir la lista resultante por pantalla.
# print(f"La lista anidada resultante es: {lista_anidada}")
