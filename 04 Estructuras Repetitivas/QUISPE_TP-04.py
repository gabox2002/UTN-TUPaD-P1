#1. Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

## Itera a través de los números del 0 al 100 (inclusive) e imprime cada uno.
## for i in range(0, 101):
##     print(i)

#2. Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# # Pedir al usuario un número entero positivo
# numero = int(input("Ingrese un número entero positivo: "))

# # Contar dígitos
# if numero == 0:
#     cantidad_digitos = 1
# else:
#     cantidad_digitos = 0
#     while numero > 0:
#         numero = numero // 10
#         cantidad_digitos += 1

# # Mostrar el resultado
# print(f"El número ingresado tiene {cantidad_digitos} dígito(s).")

#3. Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# # Pedir dos números enteros al usuario
# valor1 = int(input("Ingrese el primer número entero: "))
# valor2 = int(input("Ingrese el segundo número entero: "))

# # Asegurarse de que valor1 sea el menor y valor2 el mayor
# if valor1 > valor2:
#     valor1, valor2 = valor2, valor1  # Intercambiar valores si es necesario

# # Inicializar la suma
# suma = 0

# # Usar un bucle for para sumar los valores entre valor1 y valor2 (excluyendo los extremos)
# for i in range(valor1 + 1, valor2):
#     suma += i

# # Mostrar el resultado
# print(f"La suma de los enteros entre {valor1} y {valor2} es: {suma}")

#4. Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# # Inicializar la suma total
# suma_total = 0

# # Inicializar el número ingresado para que entre al bucle
# numero = None

# # Mientras el número ingresado no sea 0, seguir sumando
# while numero != 0:
#     numero = int(input("Ingrese un número entero (ingrese 0 para terminar): "))
    
#     # Si el número no es 0, agregarlo a la suma
#     if numero != 0:
#         suma_total += numero

# # Mostrar el total acumulado
# print(f"El total acumulado es: {suma_total}")


# 5. Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random

# numero_secreto = random.randint (0, 9)
# intentos = 0
# adivinado = False
# intento = 0
# print ("Adiviná el número secreto entre 0 y 9!")

# while intento != numero_secreto:
#     intento = int(input("Ingresá tu intento: "))
#     intentos += 1

#     if intento == numero_secreto:
#         #adivinado = True
#         print("Correcto! Adivinaste el número.")
#     else:
#         print("Incorrecto, intentá de nuevo.")
# print("Cantidad de intentos: ", intentos)


####5. segunda forma ##############################################
# import random

# numero_secreto = random.randint(0, 9)
# intentos = 0
# adivinado = False

# print("¡Adiviná el número secreto entre 0 y 9!")

# while not adivinado:
#     intento = int(input("Ingresá tu intento: "))
#     intentos += 1
#     # el contador intentos se incrementa en una unidad, intentos=intentos+1
#     if intento == numero_secreto:
#         adivinado = True
#         print("Correcto! adivinaste el número.")
#     else:
#         print("Incorrecto, intentá de nuevo.")
# print ("Cantidad de intentos:", intentos)


#6. Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# #Inicializamos la variable 'numero' con el valor de inicio (100)
# numero = 100

# # Bucle WHILE que continúa mientras 'numero' sea mayor o igual a 0.
# while numero >= 0:
#   if numero % 2 == 0:   # Condicional IF que verifica si 'numero' es par.
#     print(numero)       # Si 'numero' es par, se imprime su valor en la pantalla.
#   numero = numero - 1   # Decrementamos el valor de 'numero' en 1 en cada iteración.

#7. Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# # Solicitar al usuario que ingrese un número entero positivo
# numero = int(input("Ingrese un número entero positivo: "))

# # Verificar que el número sea positivo
# if numero < 0:
#     print("Por favor, ingrese un número entero positivo.")
# else:
#     # Inicializar la suma
#     suma_total = 0
    
#     # Usar un bucle `for` para sumar todos los números entre 0 y el número dado
#     for i in range(numero + 1):  # `numero + 1` para incluir el número ingresado
#         suma_total += i
    
#     # Mostrar el resultado
#     print(f"La suma de todos los números entre 0 y {numero} es: {suma_total}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# # Definir la cantidad de números a ingresar 
# cantidad_numeros = 100

# # Inicializar los contadores
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# # Bucle para ingresar los números
# for i in range(cantidad_numeros):
#     numero = int(input(f"Ingrese el número {i + 1} de {cantidad_numeros}: "))
    
#     # Contar pares e impares
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
    
#     # Contar positivos y negativos
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1

# # Mostrar los resultados
# print(f"\nResultados:")
# print(f"Total de números pares: {pares}")
# print(f"Total de números impares: {impares}")
# print(f"Total de números positivos: {positivos}")
# print(f"Total de números negativos: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# # Definir la cantidad de números a ingresar (100 en este caso)
# cantidad_numeros = 10

# # Inicializar la suma total
# suma_total = 0

# # Bucle para ingresar los números
# for i in range(cantidad_numeros):
#     numero = int(input(f"Ingrese el número {i + 1} de {cantidad_numeros}: "))
#     suma_total += numero  # Sumar el número ingresado

# # Calcular la media
# media = suma_total / cantidad_numeros

# # Mostrar el resultado
# print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# # Solicitar al usuario que ingrese un número entero
# numero_ingresado = input("Ingrese un número entero: ")

# # Invertir la cadena utilizando slicing (invierte la cadena)
# numero_invertido = numero_ingresado[::-1] # indica que se deben seleccionar todos los elementos, pero en orden inverso (con un paso de -1).

# # Mostrar el número invertido
# print(f"El número con los dígitos invertidos es: {numero_invertido}")