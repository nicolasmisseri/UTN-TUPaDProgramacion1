''' 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.'''

for i in range(0,101):
    print(i)

'''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad
de dígitos que contiene.'''

numero_entero = input("Ingrese un numero entero: ")
print(f"El numero ingresado contiene {len(numero_entero)} digitos")

'''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.'''

num1 = int(input("Ingrese el numero con el que comienza el rango: "))
num2 = int(input("Ingrese el numero con el que finaliza el rango: "))
suma = 0

for i in range(num1+1, num2):
    suma= suma + i
print(f"La suma total de los numeros es {suma}")

'''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario
ingrese un 0.'''

num=int(input("Ingrese un numero para sumarlo, para finalizar ingrese 0: "))
suma=0

while (num != 0) :
    suma+=num
    num=int(input("Ingrese un numero para sumarlo, para finalizar ingrese 0: "))
print(f"El total de la suma de los numeros ingresados es {suma}")

'''5)8 Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final,
el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.'''


intento = int(input("Ingrese el numero que piensa que es entre 0 y 9: "))
numero_secreto=7
contador_de_intentos= 1
while (intento != numero_secreto) :
    contador_de_intentos+=1
    intento = int(input("Ingrese el numero que piensa que es entre 0 y 9: "))
print(f"Muy bien, Acertaste! Luego de {contador_de_intentos} intentos.")

'''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.'''

for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i)
print("Impresos en pantalla todos los numeros pares de 0 a 100 de forma descendente.")

'''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.'''

final_del_rango= int(input("Ingrese un numero entero mayor a 0: "))
suma = 0

for i in range(0,final_del_rango):
    suma +=i
print(f"La suma de todos los numeros comprendidos entre 0 y el numero entero positivo indicado por el usuario es: {suma}")

'''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos
son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una
cantidad menor, pero debe estar preparado para procesar 100 números con un solo
cambio).'''

pares= 0
impares = 0
positivos = 0
negativos = 0

for i in range (0,100):
    num = int(input("Ingrese un numero para ver si es positivo, negativo, par o impar: "))
    if num % 2 == 0:
        pares+=1
    else:
        impares+=1
    if num >= 0 :
        positivos +=1
    else:
        negativos+=1
print(f"Numeros Pares: {pares}")
print(f"Numeros Impares: {impares}")
print(f"Numeros Positivos: {positivos}")
print(f"Numeros Negativos: {negativos}")

'''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule
la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero
debe poder procesar 100 números cambiando solo un valor).'''

suma=0
for i in range(0,100):
    num=int(input("Ingrese el numero a promediar: "))
    suma+=num
promedio= suma / 100

print(f"El promedio de los numeros ingresados es: {promedio}")

'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''

numero = input("Ingrese un numero para verlo invertido: ")
numero_invertido=""

for i in range(len(numero)-1,-1,-1):
    numero_invertido+=numero[i]
print(numero_invertido)















