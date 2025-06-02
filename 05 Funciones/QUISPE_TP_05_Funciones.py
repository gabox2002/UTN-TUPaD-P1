## Práctico 2: Funciones en Python

## 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# # Definimos la función
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# # Programa principal
# imprimir_hola_mundo()

## 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# # Definimos la función
# def saludar_usuario(nombre):
#   """
#   Esta función recibe un nombre como parámetro y devuelve un saludo personalizado.

#   Args:
#     nombre: El nombre de la persona a saludar.

#   Returns:
#     Una cadena de texto con el saludo personalizado.
#   """
#   return f"Hola {nombre}!"

# # Solicitar el nombre al usuario desde el programa principal
# nombre_del_usuario = input("Por favor, ingresa tu nombre: ")

# # Llamar a la función y almacenar el resultado
# saludo = saludar_usuario(nombre_del_usuario)

# # Imprimir el saludo personalizado
# print(saludo)

## 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#   """
#   Esta función recibe información personal e imprime un mensaje formateado.

#   Args:
#     nombre: El nombre de la persona.
#     apellido: El apellido de la persona.
#     edad: La edad de la persona.
#     residencia: El lugar de residencia de la persona.
#   """
#   print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# # Pedir los datos al usuario desde el programa principal 
# nombre_usuario = input("Ingresa tu nombre: ")
# apellido_usuario = input("Ingresa tu apellido: ")
# edad_usuario = input("Ingresa tu edad: ") 
# residencia_usuario = input("Ingresa tu lugar de residencia: ")

# # Llamar a la función con los valores ingresados por el usuario 
# informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

## 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# import math

# def calcular_area_circulo(radio):
#   """
#   Calcula el área de un círculo dado su radio.

#   Args:
#     radio: El radio del círculo.

#   Returns:
#     El área del círculo.
#   """
#   return math.pi * (radio ** 2)

# def calcular_perimetro_circulo(radio):
#   """
#   Calcula el perímetro de un círculo dado su radio.

#   Args:
#     radio: El radio del círculo.

#   Returns:
#     El perímetro del círculo.
#   """
#   return 2 * math.pi * radio

# # # --- Llamar a la función ---
# radio_usuario = float(input("Ingresa el radio del círculo: "))

# area = calcular_area_circulo(radio_usuario)
# perimetro = calcular_perimetro_circulo(radio_usuario)

# print(f"El área del círculo es: {area:.2f}")
# print(f"El perímetro del círculo es: {perimetro:.2f}")


## 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def segundos_a_horas(segundos):
#   """
#   Convierte una cantidad de segundos a horas.

#   Args:
#     segundos: La cantidad de segundos a convertir.

#   Returns:
#     La cantidad de horas correspondientes.
#   """
#   return segundos / 3600

# # Solicitar los segundos al usuario
# segundos = int(input("Ingresa la cantidad de segundos: "))
# horas = segundos_a_horas(segundos)
# print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

## 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#   """
#   Imprime la tabla de multiplicar de un número del 1 al 10.

#   Args:
#     numero: El número del cual se imprimirá la tabla de multiplicar.
#   """
#   print(f"Tabla de multiplicar del {numero}:")
#   for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

# # Solicitar el número al usuario
# numero_usuario = int(input("Ingresa un número para ver su tabla de multiplicar: "))
# tabla_multiplicar(numero_usuario)

## 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# def operaciones_basicas(a, b):
#   """
#   Realiza suma, resta, multiplicación y división de dos números.

#   Args:
#     a: El primer número.
#     b: El segundo número.

#   Returns:
#     Una tupla con (suma, resta, multiplicacion, division).
#     La división devuelve None si el divisor es cero.
#   """
#   return (a + b, a - b, a * b, a / b if b != 0 else "Indefinido")

# # Solicitar los números al usuario
# a = float(input("Ingresa el primer número: "))
# b = float(input("Ingresa el segundo número: "))
# suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# # Llamar a la función
# resultados = operaciones_basicas(a, b)

# print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}")

## 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calcular_imc(peso, altura):
#   """
#   Calcula el Índice de Masa Corporal (IMC).

#   Args:
#     peso: El peso en kilogramos.
#     altura: La altura en metros.

#   Returns:
#     El valor del IMC.
#   """
#   if altura <= 0:
#     return None # Evitar división por cero o altura inválida
#   return peso / (altura ** 2)

# # Solicitar los datos al usuario
# peso = float(input("Ingresa tu peso (kg): "))
# altura = float(input("Ingresa tu altura (m): "))
# imc = calcular_imc(peso, altura)
# print(f"Tu IMC es: {imc:.2f}")

## 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#   """
#   Convierte una temperatura de grados Celsius a Fahrenheit.

#   Args:
#     celsius: La temperatura en grados Celsius.

#   Returns:
#     La temperatura equivalente en Fahrenheit.
#   """
#   return (celsius * 9/5) + 32

# # Pedir la temperatura en Celsius al usuario
# celsius = float(input("Ingresa la temperatura en Celsius: "))
# fahrenheit = celsius_a_fahrenheit(celsius)
# print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

## 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función

# def calcular_promedio(a, b, c):
#   """
#   Calcula el promedio de tres números.

#   Args:
#     a: El primer número.
#     b: El segundo número.
#     c: El tercer número.

#   Returns:
#     El promedio de los tres números.
#   """
#   return (a + b + c) / 3

# # Solicitar los números al usuario
# a = float(input("Primer número: "))
# b = float(input("Segundo número: "))
# c = float(input("Tercer número: "))
    
# # Llamar a la función y mostrar el resultado
# promedio = calcular_promedio(a, b, c)
# print(f"El promedio es: {promedio:.2f}")