def main():
    contrasenia = "123456"
    usuario = input("Ingrese la contraseña: ")
    if usuario == contrasenia:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

if __name__ == "__main__":
    main()