'''
Escribir un programa que muestre un menú con las siguientes opciones:
a. Suma.
b. Multiplicación
c. Largo de Palabras
d. Salir.
Funcionamiento:
 El usuario debe ver el menú de opciones todo el tiempo.
 Si elige la opción a:
Debe solicitar 2 números, sumarlos y mostrarlos.
 Si elige opción b:
Debe solicitar 2 números, restarlos y mostrarlos.
 Si elige la opción c:
Debe solicitar 2 números, multiplicarlos y mostrarlos.
 Si elige la opción d:
Debe solicitar dos palabras y mostrar la palabra más larga, avisar cuando
sean iguales.en ambos casos debe mostrar el largo de cada una
 Si elige la opción e:
Debe salir y despedir al usuario.
'''

while True:
    opcion = input(""" INICIO 
    a.Suma
    b.Resta
    c.Mulstiplicacion
    d.Largo de la palabra
    e.Salir         
    opcion:""")
    if opcion != "a" and opcion != "b" and opcion !="c" and opcion != "d" and opcion !="e":
        print("opcion incorrecta, seleccione otra vez")
    if opcion == "a":
        num1 = int(input("ingrese el primer numero:"))
        num2 = int(input("ingrese el segundo numero:"))
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    if opcion =="b":
        num1 = int(input("ingrese el primer numero:"))
        num2 = int(input("ingrese el segundo numero:"))
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    if opcion =="c":
        num1 = int(input("ingrese el primer numero:"))
        num2 = int(input("ingrese el segundo numero:"))
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    if opcion =="d":
        text1 = input("ingrese la primera palabra:")
        text2 = input("ingrese la segunda palabra:")
        largo1 = len(text1)
        largo2 = len(text2)
        if largo1 == largo2:
            print(f"las palabras {text1} y {text2} son iguales y tienen {largo1} letras")
        elif largo1 > largo2:
            print(f"la palabra {text1} es mas larga que la palabra {text2}")
        else:
            print(f"la palabra {text2} es mas larga que {text1}")
    if opcion =="e":
        print("Fin Del Programa")
        break
