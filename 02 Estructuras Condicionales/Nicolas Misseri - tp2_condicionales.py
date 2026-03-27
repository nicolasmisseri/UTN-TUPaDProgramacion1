''' 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. '''

edad = int(input("Ingrese su edad: "))
if edad >= 18 :
    print("Es mayor de edad")
else :
    print("Es menor de edad")

''' 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. '''

nota = float(input("Ingrese su calificacion: "))
if nota >= 6 :
    print ("Aprobado")
else:
    print("Desaprobado")

'''3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. '''

num = float(input("Ingrese un numero para saber si es par o no: "))
if num % 2 == 0 :
    print("Ha ingresado un numero par")
else:
    print("Ingrese un numero par, el ingresado no lo es")

'''4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
• Niño/a: menor de 12 años.
• Adolescente: mayor o igual que 12 años y menor que 18 años.
• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
• Adulto/a: mayor o igual que 30 años.'''

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

'''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
que tiene un iterable tal como una lista o un string.'''   

password = input("Ingrese su password")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

'''6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
• Menor que 150 kWh: “Consumo bajo”.
• Entre 150 y 300 kWh (inclusive): “Consumo medio”.
• Mayor que 300 kWh: “Consumo alto”.
Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
“Considere medidas de ahorro energético”.
El programa debe imprimir por pantalla la categoría correspondiente.'''

consumo_en_kwh=int(input("Ingrese su consumo energetico en kwh: "))
if consumo_en_kwh < 150:
    print("“Consumo bajo”")
elif consumo_en_kwh < 300:
    print("Consumo medio")
elif consumo_en_kwh > 300:
    print("Consumo alto")
    if consumo_en_kwh > 500:
        print("Considere medidas de ahorro energético")

'''7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.'''

frase = input("Ingrese su frase o palabra: ")

ultima_letra= frase[len(frase)-1]

if ultima_letra == "a":
    print(frase+"!")
elif ultima_letra == "e":
    print(frase+"!")
elif ultima_letra == "i":
    print(frase+"!")
elif ultima_letra == "o":
    print(frase+"!")
elif ultima_letra == "u":
    print(frase+"!")
elif ultima_letra == "A":
    print(frase+"!")
elif ultima_letra == "E":
    print(frase+"!")
elif ultima_letra == "I":
    print(frase+"!")
elif ultima_letra == "O":
    print(frase+"!")
elif ultima_letra == "U":
    print(frase+"!")
else:
    print(frase)

'''Averigue que se puede hacer con el metodo in "aeiouAEIOU" pero no aparecia en lo apendido hasta el momento, 
si es solicitado lo puedo hacer de esa manera tambien'''

'''8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por
el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.'''

nombre = input("Ingrese su nombre: ")
print("¿Cómo quiere su nombre?")
print("1. MAYÚSCULAS (ej: PEDRO)")
print("2. minúsculas (ej: pedro)")
print("3. Primera letra mayúscula (ej: Pedro)")

eleccion = int(input("Ingrese su opción (1, 2 o 3): "))

if eleccion == 1:
    print(nombre.upper())
elif eleccion == 2: 
    print(nombre.lower())
elif eleccion == 3:
    print(nombre.title())
else:
    print("Ingrese una opcion valida")


'''9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
• Menor que 3: "Muy leve" (imperceptible).
• Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
• Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
• Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
• Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
• Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). '''

magnitud = float(input("Ingrese la magnitud del terremoto en escala de Richter: "))

if magnitud < 3 :
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else :
    print("Extremo (puede causar graves daños a gran escala)")

'''10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año: 

Periodo del Año	                    Estación (Hemisferio Norte)	    Estación (Hemisferio Sur)
21 de diciembre - 20 de marzo	    ❄️ Invierno	                    ☀️ Verano
21 de marzo - 20 de junio	        🌸 Primavera	                🍂 Otoño
21 de junio - 20 de septiembre	    ☀️ Verano	                    ❄️ Invierno
21 de septiembre - 20 de diciembre	🍂 Otoño	                    🌸 Primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano'''

dia = int(input("Ingrese el dia del 1 al 31: "))
mes = int(input("Ingrese el mes del 1 al 12: "))
hemisferio = input("Ingrese el hemisferio N o S: ").upper()

if (mes == 3 and dia <= 21) or (mes == 6 and dia <= 20) or (mes == 4 or mes == 5):
        if hemisferio == "N" : print("PRIMAVERA")
        else: print("OTOÑO")
elif (mes == 6 and dia <= 21) or (mes == 9 and dia <= 20) or (mes == 7 or mes == 8):
        if hemisferio == "N" : print("VERANO")
        else: print("INVIERNO")
elif (mes == 9 and dia <= 21) or (mes == 12 and dia <= 20) or (mes == 10 or mes == 11):
        if hemisferio == "N" : print("OTOÑO")
        else: print("PRIMAVERA")
else: # (mes == 12 and dia <= 21) or (mes == 3 and dia <= 20) or (mes == 1 or mes == 2):
        if hemisferio == "N" : print("INVIERNO")
        else: print("VERANO")












