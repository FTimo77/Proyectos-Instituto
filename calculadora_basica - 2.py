
def suma(num1, num2):
    print("El resultado es: ")
    print(num1 + num2)
def resta(num1, num2):
    print("El resultado es: ")
    print(num1 - num2)
def multiplicacion(num1, num2):
    print("El resultado es: ")
    print(num1 * num2)
def division(num1, num2):
    print("El resultado es: ")
    print(num1 / num2)

def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro número: "))
    operacion = int(input("Que operación deseas hacer\n"
                          "1 - suma\n"
                          "2 - resta\n"
                          "3 - multiplicación\n"
                          "4 -  división \n"))
    match operacion:
        case 1:
            suma(num1, num2)
        case 2:
            resta(num1, num2)
        case 3:
            multiplicacion(num1, num2)
        case 4:
            division(num1, num2)


if __name__  == "__main__":
    main()