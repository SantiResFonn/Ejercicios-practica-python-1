lista_numeros = list((input("Ingrese muchos numeros ")))
i=0
suma = []
print("Esta es su lista de numeros", lista_numeros)
for i in range(len(lista_numeros)):
    conversion = int(lista_numeros[i])
    suma.append(conversion)
    i+=1
valores_suma = sum(suma)
media = valores_suma/len(lista_numeros)
print("La media aritmetica de la lista dada es", media)