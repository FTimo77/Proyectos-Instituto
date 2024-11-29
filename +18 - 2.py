def main():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad >= 0 and edad <=12:
                print("Eres un niño")
            elif edad >= 13 and edad <= 18:
                print("Eres un adolescente")
            else:
                print("Eres mayor de edad")
            break  # Salir del bucle si no hay errores
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
