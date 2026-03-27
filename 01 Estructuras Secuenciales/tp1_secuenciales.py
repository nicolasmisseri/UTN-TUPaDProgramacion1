# ejercicio 1

print("Hola Mundo!")

# ejercicio 2

nombre= input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

# ejercicio 3

nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))  
lugar_residencia= input("Ingrese su lugar de residencia: ")
print(f"Hola, soy {nombre}. Tengo {edad} años y vivo en {lugar_residencia}.")

# ejercicio 4

import math

radio = float(input("Ingrese el radio del círculo: "))
area = round((math.pi * radio ** 2),2)
perimetro = round((2 * math.pi * radio),2)
print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# ejercicio 5

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600 # uso el cociente entero para las horas
segundos_restantes = segundos % 3600 # Uso el resto para los segundos restantes
minutos = segundos_restantes // 60 # uso el cociente entero para los minutos
segundos_finales = segundos_restantes % 60 # uso el resto para los segundos finales
print(f"{horas} horas, {minutos} minutos y {segundos_finales} segundos")

# ejercicio 6

numero = int(input("Ingrese un número para conocer su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# ejercicio 7

num1=int(input("Ingrese un numero distinto de 0:"))
num2=int(input("Ingresar otro numero distinto de 0:"))

if (num1 > 0) & (num2 > 0):
    suma = num1+num2
    division = round((num1/num2),2)
    multiplicacion = num1*num2
    resta = num1-num2

    print(f"el resultado de la suma es: {suma}")
    print(f"el resultado de la division es: {division}")
    print(f"el resultado de la multiplicacion es: {multiplicacion}")
    print(f"el resultado de la resta es: {resta}")
else: print("Ingrese solo numeros mayores a 0 por favor")

# ejercicio 8

peso = int(input("Ingrese su peso en kilogramos: "))
altura= float(input("Ingrese su altura en metros: "))

imc = round((peso / altura**2),2)

print(f"Tu indicie de masa corporal es: {imc}")

# ejercicio 9

celcius = float(input("Ingresar temperatura actual en grados celcius (°C): "))

farenheit= round((((9/5)*celcius)+32),2)

print(f"La temperatura en grados farenheit es de {farenheit}°F ")

# ejercicio 10

num1=float(input("Ingresar un numero: "))
num2=float(input("Ingresar otro numero: "))
num3=float(input("Ingresar otro numero: "))

promedio = round(((num1+num2+num3)/3),2)

print(f"El promedio de los 3 numeros ingresados es: {promedio}")
