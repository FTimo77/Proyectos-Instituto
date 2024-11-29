def main():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            if numero >= 10:
                print("El número ingresado es mayor o igual a 10")
            else:
                print("El número ingresado es menor que 10")
            break  # Salir del bucle si no hay errores
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
