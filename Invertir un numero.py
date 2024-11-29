def invertir_numero(numero):
    return int(str(numero)[::-1])

numero = int(input("Ingrese un número entero: "))
print(f"El número invertido de {numero} es {invertir_numero(numero)}.")
