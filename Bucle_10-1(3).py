def contador_regresivo():
    for i in range(10, 0, -1):  # Comienza en 10, termina en 1 (paso -1)
        print(i, end=", " if i > 1 else "\n")  # Formato de salida

def main():
    print("Contador regresivo:")
    contador_regresivo()

if __name__ == "__main__":
    main()
