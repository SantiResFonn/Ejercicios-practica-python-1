cadena_texto = list(input("Ingrese una cadena de texto: "))
i = 0
j = len(cadena_texto)-1
while (i<len(cadena_texto)):
    if(cadena_texto[i] != cadena_texto[j]):
        palindromo = False
        break
    else:
        i += 1
        j -= 1
        palindromo = True
if palindromo:
    print("La cadena de texto ingresada es palindromo")
else:
    print ("La cadena de texto ingresada no es palindromo")
