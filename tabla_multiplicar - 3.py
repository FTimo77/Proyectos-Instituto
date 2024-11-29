def main():
    digito = int(input("Ingresa el número del que deseas la tabla: "))
    for i in range(1, 11):
        resultado = digito * i
        print(str(digito) +" x " + str(i) + " = " + str(resultado))

if __name__ == "__main__":
    main()