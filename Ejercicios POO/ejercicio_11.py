import random as random
lista_pares = []
i = 1
while (i<=100):
    if (i%2==0):
        lista_pares.append(i)
        i += 1
    else:
        i += 1
print("Lista de los numeros pares del 1 al 100", lista_pares)