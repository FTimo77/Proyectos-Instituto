def main():
    while True:
        try:
            numero = int(input("Ingrese su calificación para determinar si ha sido aprobado: "))
            if numero >= 7 and numero <= 10:
                print("APROBADO")
                break
            elif numero < 7 and numero >= 0:
                print("REPROBADO")
                break
            else:
                print("Ingresa una cantidad válida")

        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
