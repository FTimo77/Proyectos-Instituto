def es_par(n):
    return n % 2 == 0

numero = int(input("Ingrese un número: "))
print(f"¿El número {numero} es par? {es_par(numero)}")
