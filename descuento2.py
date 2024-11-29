def main():
    monto = int(input("Ingrese el valor pagado para calcular el monto total \n"))
    if monto >= 100:
        monto = monto * 0.80
    print("El monto final es de " + str(monto))

if __name__ == "__main__":
    main()