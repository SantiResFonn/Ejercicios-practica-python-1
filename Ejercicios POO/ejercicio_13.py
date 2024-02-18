numero_uno = float(input("Ingrese el primer numero "))
numero_dos = float(input("Ingrese el segundo numero "))
print("La suma de ambos numeros es", numero_uno + numero_dos)
print("La resta de ambos numeros es", numero_uno - numero_dos)
print("La multiplicación de ambos numeros es", numero_uno * numero_dos)
if (numero_dos==0):
    print("No se puede dividir por cero, ingrese otro numero")
else:
    print("La división de ambos numeros es", numero_uno/numero_dos)