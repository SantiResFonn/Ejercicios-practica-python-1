lista_numeros = list((input("Ingrese muchos numeros ")))
i=0
suma = []
print("Esta es su lista de numeros", lista_numeros)
for i in range(len(lista_numeros)):
    conversion = int(lista_numeros[i])
    suma.append(conversion)
    i+=1
print("La suma de los numeros en la lista es", sum(suma))
