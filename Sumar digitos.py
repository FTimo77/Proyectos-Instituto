def sumar_digitos(numero):
    return sum(int(digito) for digito in str(numero))

numero = int(input("Ingrese un número entero: "))
print(f"La suma de los dígitos de {numero} es {sumar_digitos(numero)}.")
