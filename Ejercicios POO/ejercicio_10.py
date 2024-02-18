numero = int(input("Ingrese un numero "))
i = 1
factorial = 1
while (i<=numero):
    factorial = factorial * i
    i += 1
print("El factorial de", numero,"es",factorial)