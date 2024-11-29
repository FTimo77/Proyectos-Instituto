import random

def main():
    numero = random.randint(1, 10)
    user = int(input("Ingresa un número entre el uno al 10 e intenta adivinar la respuesta: "))
    print("El número aleatorio es " + str(numero))
    if numero == user:
        print("LO HAS ADIVINADO, FELICIDADES")
    else:
        print("Mas suerte para la próxima")


if __name__ == "__main__":
    main()