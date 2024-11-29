def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {calcular_factorial(numero)}.")
