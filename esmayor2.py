def main():
    while True:
        try:
            numero1 = int(input("Ingrese un número: "))
            numero2 = int(input("Ingrese el segundo número: "))
            numero3 = int(input("Ingrese el tercer número: "))
            if numero1 > numero2:
                if numero1 > numero3:
                    print(str(numero1) + " es el mayor")
                else:
                    print(str(numero3) + " es el mayor")
            else:
                print(str(numero2) + " es el mayor")
            break  # Salir del bucle si no hay errores
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
