lista_numeros = list((input("Ingrese muchos numeros ")))
i=0
int_lista = []
print("Esta es su lista de numeros", lista_numeros)
for i in range(len(lista_numeros)):
    conversion = int(lista_numeros[i])
    int_lista.append(conversion)
    i+=1
print("El valor maximo de la lista es", max(int_lista),"y el valor minimo de la lista es",min(int_lista))