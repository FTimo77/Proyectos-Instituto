def main():
    anio =int(input("Ingrese el año para determinar si es bisiesto: "))
    if anio %4 == 0:
        if anio %100 == 0:
            if anio %400 == 0:
                print("Es un año bisiesto")
            else:
                print("No es un año bisiesto")
        else:
            print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")

if __name__ == "__main__":
    main()