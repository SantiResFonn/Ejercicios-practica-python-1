lista_numeros = list((input("Ingrese muchos numeros ")))
i=0
j=len(lista_numeros)-1
int_lista = []
print("Esta es su lista de numeros", lista_numeros)
for i in range(len(lista_numeros)):
    conversion = (lista_numeros[j])
    int_lista.append(conversion)
    i+=1
    j-=1
print("La lista invertida es esta", int_lista)