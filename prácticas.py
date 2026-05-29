#Ejercicio 1
def multiplo():
    lista_guardar= []
    a= int(input("Ingresa un número entero: "))
    for num in range(1,11):
        lista_guardar.append(num*a)
    print(lista_guardar)
multiplo()
#Ejercicio 2 cadena de caracteres
def lectura(cadena):
    lista_de_caracteres= []
    for letra in cadena:
        if letra not in lista_de_caracteres:
            lista_de_caracteres.append(letra)
    print(lista_de_caracteres)
lectura("Hello")

#Ejercicio 3
lista_palabras=[]
tamaño= int(input("¿Cuántas palabras tendrá la lista? "))
for i in range(tamaño):
    palabra=input(f"Inserte la palabra {i+1} :")
    lista_palabras.append(palabra)
print("La lista creada es", lista_palabras)
búsqueda= input("¿Qué palabra deseas buscar? ")
contador= 0
for palabra in lista_palabras:
    if palabra == búsqueda:
        contador+= 1
print(f"La palabra {búsqueda} aparece {contador} veces")

#Ejercicio 4
lista_1= []
lista_2= []
tamaño_lista1= int(input("¿Cuántas palabras tiene la lista 1?: "))
for i in range(tamaño_lista1):
    palabraa= input(f"Escribe la palabra {i+1}:")
    lista_1.append(palabraa)
tamaño_lista2= int(input("¿Cuántas palabras tiene la lista 2? "))
for i in range(tamaño_lista2):
    palabraa= input(f"Escribe la palabra {i+1}: ")
    lista_2.append(palabraa)
for palabraa in lista_2:
    while palabraa in lista_1:
        lista_1.remove(palabraa)
    print(lista_1)
# Ejercicio 5
lista = []
n = int(input("Cantidad de palabras: "))
for i in range(n):
    palabra = input(f"Palabra {i+1}: ")
    lista.append(palabra)
resultado = []
for palabra in lista:
    if palabra not in resultado:
        resultado.append(palabra)
print("Lista sin repetidos:", resultado
# Ejercicio 6
def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida
print("Lista invertida:", invertir_lista(numeros))
# 7. Obtener el mayor elemento usando while
def mayor_lista(lista):
    mayor = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > mayor:
            mayor = lista[i]
        i += 1
    return mayor
numeros = [8, 2, 15, 4, 10]
print("Mayor elemento:", mayor_lista(numeros))
# 8. Multiplicación índice por índice de dos listas
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
resultado = []
for i in range(len(lista1)):
    resultado.append(lista1[i] * lista2[i])
print("Resultado:", resultado)
