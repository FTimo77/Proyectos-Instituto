def main():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad  >= 18:
                print("Puedes votar")
            else:
                print("No puedes votar")
            break  # Salir del bucle si no hay errores
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
