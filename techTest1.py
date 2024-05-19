'''
Escribir un programa que solicite una frase al usuario y luego una letra, usando
while y lo aprendido sobre string en las clases anteriores, acceso a cada carácter
de una cadena por medio del elemento palabra[0], (no use IN).
Buscar si la letra que ingresó se encuentra en la frase solicitada.
Cuente cuántas veces está esa letra dentro de la frase
- Sí, esta mostrará un mensaje que diga “letra ... encontrada aparece ...
veces.
- Si no está mostrara “Letra ... no encontrada en la frase”
Luego de resolver debe preguntar al usuario si quiere salir debe ingresar una letra
“S” o si presiona cualquier otra letra continuará.
'''
while True:
    frase = input("ingrese una frase:")
    letra = input("ingrese una letra:")
    
    contador = 0
    encontrado = False
    i = 0
    
    while i < len(frase):
        if frase[i] == letra:
            contador += 1
            encontrado = True
        i += 1
    
    if encontrado:
        print(f"La letra {letra} se encontro {contador} veces en la frase")
    else:
        print(f"La letra {letra} no se encontro en la frase")
        
    opcion = input("desea seguir en el programa? presione 's' si desea salir sino cualquier otra tecla:")
    if opcion == 's':
        print("Fin Del Programa")
        break