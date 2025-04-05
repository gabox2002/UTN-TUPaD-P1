#TP CONDICIONALES - Gabriel Quispe

#Práctico 3: Estructuras condicionales

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Introduce tu edad: "))

# if edad >= 18:
#     print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# nota = float(input("Introduce tu nota: "))

# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Ingresa un número entero: "))

# if numero % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Introduce tu edad: "))

# if edad < 12:
#     print("Niño/a")
# elif edad < 18:
#     print("Adolescente")
# elif edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

# contraseña = input("Introduce tu contraseña: ")

# if 8 <= len(contraseña) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:

# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)

#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


# import random
# from statistics import mode, median, mean

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# media_lista = mean(numeros_aleatorios)
# mediana_lista = median(numeros_aleatorios)
# moda_lista = mode(numeros_aleatorios)

# print(f"Media: {media_lista}")
# print(f"Mediana: {mediana_lista}")
# print(f"Moda: {moda_lista}")

# if media_lista > mediana_lista > moda_lista:
#     print("Sesgo positivo o a la derecha")
# elif media_lista < mediana_lista < moda_lista:
#     print("Sesgo negativo o a la izquierda")
# else:
#     print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# frase = input("Introduce una frase o palabra: ")

# vocales = "aeiouAEIOU"

# if frase and frase[-1] in vocales:
#     print(frase + "!")
# else:
#     print(frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas 

# nombre = input("Introduce tu nombre: ")
# opcion = int(input("Elige una opción:\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\nOpción: "))

# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.title())
# else:
#     print("Opción inválida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

# magnitud = float(input("Introduce la magnitud del terremoto: "))

# if magnitud < 3:
#     print("Muy leve (imperceptible)")
# elif magnitud < 4:
#     print("Leve (ligeramente perceptible)")
# elif magnitud < 5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud < 6:
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif magnitud < 7:
#     print("Muy Fuerte (puede causar daños significativos)")
# else:
#     print("Extremo (puede causar graves daños a gran escala)")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Periodo del año                                                 Estación en el hemisferio norte         Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos)       Invierno                                Verano 
# Desde el 21 de marzo hasta el 20 de junio (incluidos)           Primavera                               Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos)      Verano                                  Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)  Otoño                                   Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# hemisferio = input("¿En qué hemisferio te encuentras? (Norte/Sur): ").upper()
# mes = int(input("¿Qué mes del año es? (1-12): "))
# dia = int(input("¿Qué día del mes es? (1-31): "))

# if hemisferio == "NORTE":
#     if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
#         print("Invierno")
#     elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
#         print("Primavera")
#     elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
#         print("Verano")
#     else:
#         print("Otoño")
# elif hemisferio == "SUR":
#     if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
#         print("Verano")
#     elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
#         print("Otoño")
#     elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
#         print("Invierno")
#     else:
#         print("Primavera")
# else:
#     print("Hemisferio inválido")