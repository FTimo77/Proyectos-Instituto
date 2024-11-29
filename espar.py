def main():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            if numero %2 == 0:
                print("El número ingresado es par")
            else:
                print("El número ingresado es impar")
            break  # Salir del bucle si no hay errores
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
